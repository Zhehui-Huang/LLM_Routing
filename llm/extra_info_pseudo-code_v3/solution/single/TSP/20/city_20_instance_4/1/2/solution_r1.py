import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations
import networkx as nx

# Cities' coordinates
cities = {0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
          5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
          10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73),
          14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
          18: (64, 72), 19: (14, 89)}

# Calculate distances between each city
def calculate_distances(cities):
    distances = {}
    for i, j in combinations(cities.keys(), 2):
        d = euclidean(cities[i], cities[j])
        distances[(i, j)] = distances[(j, i)] = d
    return distances

distances = calculate_distances(cities)

# Create the complete graph
G = nx.Graph()
G.add_nodes_from(cities.keys())
for (i, j), d in distances.items():
    G.add_edge(i, j, weight=d)

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Extract vertices with odd degree from T
node_degrees = T.degree()
nodes_with_odd_degree = [node for node, degree in node_degrees if degree % 2 == 1]

# Step 3: Minimum weight perfect matching within nodes with an odd degree
O = G.subgraph(nodes_with_odd_degree)
min_weight_matching = nx.algorithms.matching.min_weight_matching(O, maxcardinality=True, weight='weight')

# Step 4: Combine edges of MST and minimum weight match to make a multigraph
H = nx.MultiGraph(T)
H.add_edges_from(min_bc_weight_matching)

# Step 5: Find an Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Converting Eulerian to Hamiltonian path and compute cost
visited = set()
hamiltonian_circuit = [0]  # Start at the depot
prev = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)
        prev = v

# Ensure to return back to the starting point
hamiltonian_circuit.append(0)
total_distance = sum(distances[(hamiltonian_circuit[i], hamiltonian_circuit[i+1])] for i in range(len(hamiltonian_circuit)-1))

# Output the tour and total tour cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)