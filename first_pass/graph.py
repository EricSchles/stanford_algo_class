import random

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self,nbr,weight=0):
        self.connected_to[nbr] = weight
        
    def __str__(self):
        return str(self.id) + ' connected to ' + str([x.id for x in self.connected_to])
    
    def get_connections(self):
        return self.connected_to.keys()

    def remove_connections(self,vertex):
        try:
            del self.connected_to[vertex]
        except KeyError:
            pass
            
    def get_id(self):
        return self.id

    def get_weight(self,nbr):
        return self.connected_to[nbr]

class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

    def add_vertex(self,key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def remove_connections(self,key):
        to_remove = self.vertex_list[key]
        for v in self.vertex_list.keys():
            vertex = self.vertex_list[v]
            vertex.remove_connections(to_remove)

    def remove_vertex(self,key):
        self.num_vertices -= 1
        try:
            to_remove = self.get_vertex(key)
            edges = self.get_edges(key)
            self.remove_connections(key)
            del self.vertex_list[to_remove.id]
            return to_remove,edges
        except KeyError:
            pass

    def get_vertex(self,vertex_key):
        if vertex_key in self.vertex_list.keys():
            return self.vertex_list[vertex_key]
        else:
            return None

    def __contains__(self,vertex_key):
        return vertex_key in self.vertex_list.keys()

    def add_edge(self,from_vertex,to_vertex,cost=0):
        #if not from_vertex in self.vertex_list:
        #    self.add_vertex(from_vertex)
        #if not to_vertex in self.vertex_list:
        #    self.add_vertex(to_vertex)
        self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex],cost)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())

    def get_edges(self,key):
        edges = []
        for v in self:
            for w in v.get_connections():
                if key == w.get_id() or key == v.get_id():
                    edges.append( (v.get_id(),w.get_id()) )
        return edges
    
    def get_all_edges(self):
        edges = []
        for v in self:
            for w in v.get_connections():
                edges.append( (v.get_id(),w.get_id()) )
        return edges

    

    
def generate_random_graph():
    g = Graph()
    size_of_graph = random.randint(100,150)
    for i in range(size_of_graph):
        g.add_vertex(i)
    for i in range(size_of_graph//2):
        start = random.randint(0,size_of_graph)
        finish = random.randint(0,size_of_graph)
        g.add_edge(start,finish)
    return g
