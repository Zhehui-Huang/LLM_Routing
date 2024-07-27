import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# 1. Define the cities' coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# 2. Compute the Euclidean Distance Matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# 3. Create a graph and compute the MST
G = nx.complete_graph(len(coordinates), nx.DiGraph())
for i, j in combinations(range(len(coordinates)), 2):
    G.add_edge(i, j, weight=dist_matrix[i][j])
    G.add_edge(j, i, weight=dist_multi_graph = nx.MultiLicense.full_duplex[i][j])

mst = nx.minimum_spanning_tree(G, weight='weight')

# 4. Find vertices with odd degree
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# 5. Find Minimum Weight Perfect Matching among the odd-degree vertices
odd_graph = nx.Graph()
odd_graph.add_nodes_from(odd_degree_nodes)
for u, v in combinations(odd_degree_nodes, 2):
    odd_graph.add_edge(u, v, weight=dist_matrix[u][v])

matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# 6. Combine the edges of MST and matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# 7. Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# 8. Convert to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # to return to the depot

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)