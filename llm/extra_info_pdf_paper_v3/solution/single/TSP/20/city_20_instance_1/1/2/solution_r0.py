import math
from itertools import combinations
import networkx as nx

# Function to calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Cities coordinates
city_locations = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Create graph
G = nx.Graph()

# Add nodes and edges with weights
for i in city_locations.keys():
    for j in city_counter[i:]:
        if i != j:
            G.add_edge(i, j, weight=calculate_distance(city_locations[i], city_locations[j]))

# Step 1: Construct Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices of odd degree
odd_degree_nodes = [v for v, d in mst.degree if d % 2 != 0]

# Step 3: Minimum Cost Perfect Matching on the induced subgraph of odd degree vertices
odd_graph = G.subgraph(odd_degree_nodes)
min_cost_matching = nx.algorithms.matching.min_weight_matching(odd_graph, True, weight='weight')
mst.add_edges_from(min_cost_matching)

# Step 4: Form an Eulerian circuit (Ensure every node is even degree)
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 5: Making the circuit Hamiltonian by skipping visited nodes (shortcutting)
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Return to start to complete the circuit
hamiltonian_circuit.append(0)

# Calculate the total cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)