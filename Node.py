'''
Jose Escobar
UTEP ID 80536060
CS3 Lab 6: Kruskal's and Topological sort implementation
'''

class Vertex:
    def __init__(self, label):
        self.label = label


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            if vertex.label == vertex_label:
                return vertex
        return None

def disjoint_set(graph): #DSF creator
    sets[graph] = graph
    vertices[graph] = 0

def find(graph): #Find subsets on graph
    if sets[graph] != graph:
        sets[graph] = find(sets[graph])
    return sets[graph]

def union(s1, s2): #Union of sets
    ra = find(s1)
    rb = find(s2)
    if ra != rb: 
        if vertices[ra] > vertices[rb] or vertices[ra] < vertices[rb]:
            sets[rb] = ra
        if vertices[ra] == vertices[rb]:  # If vertices are the same then increment both vertices
            vertices[ra] += 1
            vertices[rb] += 1


# The Topological sort function is from ZyBook
def get_incoming_edge_count(edge_list, vertex):
    count = 0
    for (from_vertex, to_vertex) in edge_list:
        if to_vertex is vertex:
            count += 1
    return count


def topological_sort(graph):
    result_list = []

    e = []

    for vertex in graph.adjacency_list.keys():
        if get_incoming_edge_count(graph.edge_weights.keys(), vertex) == 0:
            e.append(vertex)

    remaining_edges = set(graph.edge_weights.keys())  # starts with all edges
    while len(e) is not 0:
        curr_vertex = e.pop()  # select next vertex
        result_list.append(curr_vertex)
        outgoing_edges = []

        # remove current vertex outgoing edges from remaining edges
        for to_vertex in graph.adjacency_list[curr_vertex]:
            outgoing_edge = (curr_vertex, to_vertex)

            if outgoing_edge in remaining_edges:
                outgoing_edges.append(outgoing_edge)
                remaining_edges.remove(outgoing_edge)

        # check if removing outgoing edges creates new vertices with no incoming edges
        for (from_vertex, to_vertex) in outgoing_edges:
            in_count = get_incoming_edge_count(remaining_edges, to_vertex)
            if in_count == 0:
                e.append(to_vertex)

    return result_list 


sets = {}       # Create an empty set dict
vertices = {}   # Create an empty vertex dict


#Kruskal's minimum spanning tree algorithm
def kruskal(graph):
    global dsf, tree_edges
    for i in graph['vertex']: #Minimum spanning tree on vertices
        disjoint_set(i)
        tree_edges = list(graph['edges'])
        tree_edges.sort()
        dsf = set()

    for j in tree_edges: #Minimum spanning tree of the edges
        w, vertex_s1, vertex_s2 = j  # Weight, vertex_1, vertex_2
        if find(vertex_s1) != find(vertex_s2):
            union(vertex_s1, vertex_s2)

            dsf.add(j)  

    return sorted(dsf)
    