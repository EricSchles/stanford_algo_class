class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
    def add_vertex(self,name):
        self.vertices.append(name)
    def add_edge(self,from_vertex,to_vertex):
        self.edges.append((from_vertex,to_vertex))


