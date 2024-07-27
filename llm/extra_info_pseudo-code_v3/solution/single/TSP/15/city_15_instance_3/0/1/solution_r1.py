import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_graph(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')
                
    return dist_matrix

cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Create complete graph with Euclidean distances
dist_matrix = create_graph(cities)

# Compute Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix)
mst = mst.toarray().astype(float)

G_mst = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        if mst[i][j] > 0:
            G_mst.add_edge(i, j, weight=mst[i][j])

# Identify vertices with odd degree
odd_degree_nodes = [v for v in G_mst.nodes() if G_mst.degree(v) % 2 == 1]

# Find minimum weight perfect matching for odd degree vertices
subgraph = G_mst.subgraph(odd_degree_nodes)
min_weight_matching = nx.Graph()
min_weight_matching.add_nodes_from(subgraph.nodes())
for u in subgraph.nodes():
    min_length = float('inf')
    closest_node = None
    for v in subgraph.nodes():
        if u != v and (dist_matrix[u][v] < min_length):
            min_length = dist_matrix[u][v]
            closest_node = v
    if closest_node:
        min_weight_matching.add_edge(u, closest_node, weight=min_length)

# Combine the edges of MST and min-weight matching to form multigraph
multi_graph = nx.MultiGraph(G_mst)
multi_graph.add_edges_from(min_weight_matching.edges(data=True))

# Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Make Hamiltonian path (simple visit)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Complete the tour by returning to the start
hamiltonian_circuit.append(0)

# Compute the total cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

print("Tour:", hamiltonian_circuit)
print("Total Travel Cost:", total_cost)