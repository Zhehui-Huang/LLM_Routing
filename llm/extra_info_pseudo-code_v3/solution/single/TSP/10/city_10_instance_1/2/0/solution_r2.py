import itertools
import networkx as nx
import math

# Define the cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Compute Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a complete graph
G = nx.Graph()
for pair in itertools.combinations(cities.keys(), 2):
    G.add_edge(pair[0], pair[1], weight=distance(pair[0], pair[1]))

# Minimum spanning tree using Prim's algorithm
T = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in T
O = [v for v, d in T.degree() if d % 2 == 1]

# Subgraph induced by O
GO = G.subgraph(O)

# Minimum-weight perfect matching in O
M = nx.algorithms.matching.min_weight_matching(GO, maxcardinality=True, weight='weight')

# Create a multigraph H by combining T and M
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Convert Eulerian circuit to Hamiltonian circuit (skip repeated vertices)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if not visited:
        # Append starting point
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure the tour ends at the depot
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Compute the total cost of the tour
total_cost = 0
for i in range(len(hamiltonian_circuit) - 1):
    total_cost += distance(hamiltonian_circuit[i], hamiltonian_circuit[i + 1])

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")