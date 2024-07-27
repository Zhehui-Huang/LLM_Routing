import math
import networkx as nx
from scipy.spatial import distance
from itertools import combinations

# Cities coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance
def euclidean(c1, c2):
    return math.dist(cities[c1], cities[c2])

# Graph initialization
G = nx.Graph()
for c1, c2 in combinations(cities, 2):
    G.add_edge(c1, c2, weight=euclidean(c1, c2))

# Step 1: Compute a minimum spanning tree T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Find the odd degree vertices in T
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Minimum-weight perfect matching in the induced subgraph
min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_degree_even_nodes), maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit (skip revisited)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if not visited or u not in visited:
        hamiltonian_circuit.append(u)
    visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # to return to the starting point

# Computing the total travel cost
total_cost = sum(euclidean(hamiltonian_circuit[i], hamiltonian_circuit[i + 1]) for i in range(len(hamiltonian_circuit) - 1))

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")