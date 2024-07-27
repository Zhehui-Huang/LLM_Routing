import networkx as nx
import math
from itertools import combinations

# City coordinates
coordinates = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 
    4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31), 
    8: (61, 90), 9: (42, 49)
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete weighted graph
G = nx.Graph()
for node in coordinates:
    G.add_node(node)
for (node1, node2) in combinations(coordinates, 2):
    G.add_edge(node1, node2, weight=euclidean_distance(coordinates[node1], coordinates[node2]))

# Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find nodes with odd degree in MST
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Create a subgraph for these odd-degree nodes
odd_graph = nx.Graph()
odd_graph.add_nodes_from(odd_degree_nodes)
for (node1, node2) in combinations(odd_degree_nodes, 2):
    odd_graph.add_edge(node1, node2, weight=euclidean_distance(coordinates[node1], coordinates[node2]))

# Find minimum weight perfect matching to make degrees even
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add the matching edges to MST
mst.add_edges_from(matching)

# Create an Eulerian circuit from the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path (remove revisits)
visited = set()
hamiltonian_path = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
hamiltonian_path.append(hamiltonian_path[0])

# Compute the total cost of the final tour
total_cost = sum(euclidean_distance(coordinates[hamiltonian_path[i]], coordinates[hamiltonian_path[i+1]]) 
                 for i in range(len(hamiltonian_path) - 1))

# Output results
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)