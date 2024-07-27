import math
import networkx as nx
from itertools import combinations

# Cities with their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance
def euclidean(c1, c2):
    xy1 = cities[c1]
    xy2 = cities[c2]
    return math.sqrt((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2)

# Create an undirected graph
G = nx.Graph()
for c1, c2 in combinations(cities.keys(), 2):
    G.add_edge(c1, c2, weight=euclidean(c1, c2))

# Step 1: Compute a minimum spanning tree T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Find nodes with odd degree
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find minimum weight matching for odd degree nodes
odd_degree_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True, weight='weight')

# Step 4: Create a multigraph by combining T and M
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H))

# Remove repeated nodes to create a Hamiltonian circuit (shortcutting)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate total travel cost
total_cost = sum(euclidean(hamiltonian_circuit[i], hamiltonian_circuit[i + 1]) for i in range(len(hamiltonian_circuit) - 1))

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")