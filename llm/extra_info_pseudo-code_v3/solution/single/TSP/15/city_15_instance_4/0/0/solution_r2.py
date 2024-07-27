import math
import networkx as nx
from itertools import combinations

# Define the cities
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Create a complete graph
G = nx.Graph()
for u, v in combinations(cities, 2):
    G.add_edge(u, v, weight=distance(u, v))

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with an odd degree in MST
O = [v for v in T.nodes if T.degree(v) % 2 == 1]

# Step 3: Find a minimum weight perfect matching in the induced subgraph on vertices with odd degree
O_subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True)

# Step 4: Add edges from the matching to the MST to form a multigraph H
H = T.copy()
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Add the starting city to close the loop

# Calculate the tour cost
total_cost = sum(distance(hamiltonian_circuit[i], hamiltonian_circuit[i + 1]) for i in range(len(hamiltonian_circuit) - 1))

# Print the outcome
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")