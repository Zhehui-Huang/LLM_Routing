import math
import networkx as nx
from scipy.spatial.distance import pdist, squareform

# Define city coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Calculate pairwise Euclidean distances and create distance matrix
distance_matrix = squareform(pdist(cities, 'euclidean'))

# Steps:
# 1. Create a complete graph
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(len(cities)):
        G[i][j]['weight'] = distance_matrix[i][j]

# 2. Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# 3. Find vertices of odd degree in the MST
odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 == 1]

# 4. Create a minimum weight matching for odd-degree nodes in the MST
odd_graph = nx.Graph()
odd_graph.add_nodes_from(odd_degree_nodes)
for i in odd_degree_nodes:
    for j in odd_degree_nodes:
        if i != j:
            odd_graph.add_edge(i, j, weight=distance_matrix[i][j])
matching = nx.algorithms.matching.min_weight_matching(odd_graph, True, weight='weight')

# 5. Combine the edges of MST and the matching to make it Eulerian
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# 6. Create an Eulerian circuit
eulerian_circuit = nx.eulerian_circuit(multi_graph, source=0)
circuit = [0]

# 7. Convert Eulerian circuit to a Hamiltonian path
visited = set([0])
for u, v in eulerian_circuit:
    if v not in visited:
        circuit.append(v)
        visited.add(v)
circuit.append(0)  # Returning to the depot

# 8. Calculate the total travel cost
total_cost = sum(distance_matrix[circuit[i]][circuit[i+1]] for i in range(len(circuit)-1))

# Output
print("Tour:", circuit)
print("Total travel cost:", total_cost)