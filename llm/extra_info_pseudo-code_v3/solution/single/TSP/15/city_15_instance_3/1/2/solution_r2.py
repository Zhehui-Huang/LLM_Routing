import math
import networkx as nx

# Coordinates of the cities starting with the depot city
cities = [
    (16, 90),
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Helper function to compute Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.hypot(c1[0] - c2[0], c1[1] - c2[1])

# Create a complete graph with weights as Euclidean distances
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Identify vertices with odd degree
O = [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Create a graph induced by odd degree vertices
induced_graph = G.subgraph(O)

# Find a minimum-weight perfect matching in the induced subgraph
M = nx.algorithms.matching.min_weight_matching(induced_graph, maxcardinality=True, weight='weight')

# Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Find an Eulerian circuit on multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert the Eulerian circuit to a single-visitation Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Calculate the total travel cost of the final tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")