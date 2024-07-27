import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations
import networkx as nx

# Cities' coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73),
    14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Compute distances between each pair of cities
def calculate_distances(cities):
    distances = {}
    for i, j in combinations(cities, 2):
        distances[(i, j)] = distances[(j, i)] = euclidean(cities[i], cities[j])
    return distances

distances = calculate_distances(cities)

# Create a graph
G = nx.Graph()
G.add_nodes_from(cities.keys())
for (i, j), d in distances.items():
    G.add_edge(i, j, weight=d)

# Step 1: Compute a minimum spanning tree
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in the MST
nodes_odd_degree = [v for v in T.degree() if v[1] % 2 == 1]

# Step 3: Minimum weight perfect matching in the subgraph induced by odd degree vertices
O = G.subgraph([v[0] for v in nodes_odd_degree])
min_weight_matching = nx.algorithms.matching.min_weight_matching(O, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and min_weight_matching to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
euler_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert Eulerian to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
total_distance = 0
prev_node = 0

for u, v in euler_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)
        total_distance += G[prev_node][v]['weight']
        prev_node = v

hamiltonian_circuit.append(0)  # Return to the depot
total_distance += G[prev_node][0]['weight']  # Cost to return to start

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)