import numpy as np
from scipy.spatial.distance import euclidean
import networkx as nx

# Define the cities' coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 49),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 90)
}

# Function to calculate distances
def calculate_distances(cities):
    distances = {}
    for i in cities:
        for j in cities:
            if i != j:
                distances[(i, j)] = euclidean(cities[i], cities[j])
    return distances

distances = calculate_distances(cities)

# Constructing the complete graph
G = nx.Graph()
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            G.add_edge(i, j, weight=distances[(i, j)])

# Step 1: Compute a Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices of odd degree
odd_vertex = [node for node in mst.nodes() if mst.degree[node] % 2 == 1]

# Step 3: Minimum weight perfect matching
O = G.subgraph(odd_vertex)
min_weight_matching = nx.algorithms.matching.min_weight_matching(O, maxcardinality=True, weight='weight')

# Step 4: Create the multigraph
H = mst.copy()
H.add_edges_from(min_weight_matching)

# Step 5: Find Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert Eulerian Circuit to Hamiltonian Circuit
visited = set()
hamiltonian_circuit = [0]
last_visited = 0

for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
    last_visited = v
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the total travel cost of the Hamiltonian circuit
total_cost = sum(distances[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)