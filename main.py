'''
Jose Escobar
UTEP ID 80536060
CS3 Lab 6: Kruskal's and Topological sort implementation
'''

import Node
from Node import Graph, Vertex


g = Graph()
#Topological sort test
vertex_A = Vertex('A')
vertex_B = Vertex('B')
vertex_C = Vertex('C')
vertex_D = Vertex('D')
vertex_E = Vertex('E')
vertex_F = Vertex('F')
vertex_G = Vertex('G')

g.add_vertex(vertex_A)
g.add_vertex(vertex_B)
g.add_vertex(vertex_C)
g.add_vertex(vertex_D)
g.add_vertex(vertex_E)
g.add_vertex(vertex_F)
g.add_vertex(vertex_G)

g.add_directed_edge(vertex_A, vertex_B)
g.add_directed_edge(vertex_A, vertex_C)
g.add_directed_edge(vertex_B, vertex_F)
g.add_directed_edge(vertex_C, vertex_D)
g.add_directed_edge(vertex_D, vertex_F)
g.add_directed_edge(vertex_E, vertex_F)
g.add_directed_edge(vertex_E, vertex_G)
g.add_directed_edge(vertex_F, vertex_G)

result_list = Node.topological_sort(g)
print("Topological Sort Algorithm: ")
first = True
for vertex in result_list:
    if first:
        first = False
    else:
        print(' -> ', end='')  
    print(vertex.label, end='')


print ("\n")
#Kruskal's minimum spanning tree test
print("Kruskal's Algorithm: ")
graph2 = dict(vertex=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
edges={(15, 'A', 'B'),(6, 'A', 'D'),(9, 'B', 'C'),(12, 'B', 'D'),(14, 'B', 'G'),(10, 'B', 'H'),(16, 'C', 'E'),(8, 'D', 'E'),(20, 'E', 'F')})

graph3 = dict(vertex=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'P'],
edges={(80, 'A', 'B'),(105, 'A', 'C'),(182, 'A', 'E'),(90, 'B', 'C'),(60, 'B', 'D'),(100, 'B', 'P'),(132, 'C', 'P'),(80, 'D', 'E'),(70, 'E', 'F'),(72, 'F', 'G'),(145, 'F', 'P'),(180, 'G', 'P')})


print("Edges in minimum spanning tree (graph 1): ", "\n", (Node.kruskal(graph2)))
print("Edges in minimum spanning tree (graph 2): ", "\n", (Node.kruskal(graph3)))
