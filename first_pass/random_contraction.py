import random
from graph import Graph, generate_random_graph, Vertex
import time
def update_edges(master_edge,edges):
    new_edges = []
    for edge in edges:
        if master_edge[1] in edge:
            if edge.index(master_edge[1]) == 0:
                new_edges.append((master_edge[1],edge[1]))
            else:
                new_edges.append((edge[0],master_edge[1]))
        else:
            new_edges.append(edge)
    return new_edges

def choice(removed_vertex,removed_edges,A,B):
    vertex_id = removed_vertex.get_id()
    no_connection = True
    for edge in removed_edges:
        if edge[0] in A or edge[1] in A:
            A.append(vertex_id)
            no_connection = False
            break
        elif edge[0] in B or edge[1] in B:
            B.append(vertex_id)
            no_connection = False
            break
    if no_connection:
        if random.choice([0,1]) == 1:
            A.append(vertex_id)
        else:
            B.append(vertex_id)
    return A,B
        
def random_contraction(g):
    A,B = Vertex(),Vertex()
    A_ids,B_ids = [],[]
    while len(g.get_vertices()) > 2:
        print("num verticies",g.num_vertices)
        time.sleep(1)
        edge = random.choice(g.get_all_edges())
        start_edges = g.get_edges(edge[0])
        end_edges = g.get_edges(edge[1])
        g.remove_vertex(edge[0])
        removed_vertex,removed_edges = g.remove_vertex(edge[1])
        print("num verticies",g.num_vertices)
        A,B = choice(removed_vertex,removed_edges,A,B)
        g.add_vertex(edge[0])
        start_edges = update_edges(edge,start_edges)
        end_edges = update_edges(edge,end_edges)
        for edge in start_edges:
            g.add_edge(edge[0],edge[1])
        for edge in end_edges:
            g.add_edge(edge[0],edge[1])
    return A,B,g.get_all_edges()

A,B,edges = random_contraction(generate_random_graph())
import code
code.interact(local=locals())
