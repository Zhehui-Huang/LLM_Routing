import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate distances between each pair of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = {}
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            dist = euclidean(cities[i], cities[j])
            distances[(i, j)] = dist
            distances[(j, i)] = dist
    return distances

distances = calculate_messages(cities)

# Step 1: Compute an MST
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distances[(i, j)])

mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Find minimum weight perfect matching on odd degree nodes
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 4: Add minimum weight perfect matching to MST
mst.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
# Make sure to return to the start
hamiltonian_circuit.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(distances[(hamiltonian_circuit[i], hamiltonian_circuit[i + 1])] for i in range(len(hamiltonian_circuit) - 1))

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")