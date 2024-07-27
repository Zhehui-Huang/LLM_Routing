import math
import networkx as nx
from itertools import combinations

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Step 1: Create the complete graph
G = nx.Graph()
for (city1, coord1), (city2, coord2) in combinations(cities.items(), 2):
    G.add_edge(city1, city2, weight=euclidean_distance(coord1, coord2))

# Step 2: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 3: Identify the set O of vertices with odd degree in T
O = [v for v, d in T.degree() if d % 2 == 1]

# Step 4: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 5: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 6: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 7: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # returning to the depot

# Calculate total travel cost
total_cost = 0
for i in range(len(hamiltonian_circuit) - 1):
    total_cost += G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight']

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")