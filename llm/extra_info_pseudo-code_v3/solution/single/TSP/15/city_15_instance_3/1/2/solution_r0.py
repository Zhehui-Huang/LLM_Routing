import math
import networkx as nx
from scipy.spatial import distance
from itertools import combinations

# The coordinates of the cities starting with the depot city
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
    return math.dist(c1, c2)

# Step 1: Create a complete graph with weights as Euclidean distances
G = nx.Graph()
number_of_cities = len(cities)
for i in range(number_of_cities):
    for j in range(i + 1, number_of_cities):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 2: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Identify vertices with odd degree
O = [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Step 4a: Create a graph induced by odd degree vertices
induced_graph = G.subgraph(O)

# Step 4b: Find a minimum-weight perfect matching
M = nx.algorithms.matching.min_weight_matching(induced_graph, True, weight='weight')

# Step 5: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 6: Find an Eulerian circuit on multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert the Eulerian circuit to a single-visitation Hamiltonian path
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # return to the depot city

# Calculate the total travel cost of the final tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")