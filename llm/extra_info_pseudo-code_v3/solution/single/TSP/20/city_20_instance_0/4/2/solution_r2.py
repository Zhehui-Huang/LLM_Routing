import math
import networkx as nx
from itertools import combinations

# Define the city positions
cities_positions = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Calculate Euclidean distance function
def get_distance(city1, city2):
    x1, y1 = cities_positions[city1]
    x2, y2 = cities_positions[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Creating the complete graph
G = nx.Graph()
for a, b in combinations(cities_positions, 2):
    G.add_edge(a, b, weight=get_distance(a, b))

# Step 1: Minimum spanning tree
T = nx.minimum_spanning_tree(G)

# Step 2: Vertices with odd degree
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Minimum weight perfect matching on the induced subgraph on vertices O
O_subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True)

# Step 4: Combine edges of T and M
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Make it Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Append the start node to complete the circuit
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total distance
total_distance = 0
for i in range(len(hamiltonian_circuit) - 1):
    total_distance += get_distance(hamiltonian_circuit[i], hamiltonian_circuit[i+1])

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)