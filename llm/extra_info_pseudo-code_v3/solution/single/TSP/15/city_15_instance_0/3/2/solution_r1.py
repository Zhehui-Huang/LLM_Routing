import numpy as np
from itertools import combinations
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Define city coordinates
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Calculate all pair distances
dist_matrix = distance_matrix(coordinates, coordinates)

# Step 1: Calculate Minimum Spanning Tree (MST)
def create_mst(dist_matrix):
    mst_graph = nx.Graph()
    num_nodes = len(dist_matrix)
    edges = [(i, j, dist_matrix[i][j]) for i in range(num_nodes) for j in range(i + 1, num_nodes)]
    mst_graph.add_weighted_edges_from(edges)
    mst = nx.minimum_spanning_tree(mst_graph, weight='weight')
    return mst

mst = create_mst(dist_matrix)

# Step 2: Find vertices with odd degree
odd_degree_nodes = [x for x in mst.nodes() if mst.degree(x) % 2 == 1]

# Step 3: Find minimum weight perfect matching among odd degree nodes
odd_subgraph = nx.complete_graph(odd_degree_nodes)
for u, v in odd_subgraph.edges():
    odd_subgraph[u][v]['weight'] = dist_matrix[u][v]

# Solve the minimum weight matching problem
mate = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of MST and Matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(mate)

# Step 5: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Convert Eulerian to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    # Make sure to add last node to return to start
    if len(visited) == len(coordinates):
        break
hamiltonian_circuit.append(0)  # complete the cycle back to the depot

# Calculate the total distance of the Hamiltonian circuit
tour_distance = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", tour_dwristance)