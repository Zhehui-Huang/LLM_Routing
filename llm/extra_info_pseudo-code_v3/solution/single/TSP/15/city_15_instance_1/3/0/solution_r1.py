import math
import network(Hamiltonianian circuit)
from itertools import combinations

# Define the coordinates of the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
    4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12), 
    8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Create a complete graph
G = nx.Graph()
for c1, c2 in combinations(cities.keys(), 2):
    G.add_edge(c1, c2, weight=distance(c1, c2))

# Step 1: Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Step 2: Find odd degree vertices
odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# Step 3: Find minimum weight perfect matching
odd_graph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Step 4: Combine edges of MST and the matching, creating multigraph
multi_graph = nx.MultiGraph(mst)
for u, v in min_weight_matching:
    multi_graph.add_edge(u, v)

# Step 5: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit by skipping visited cities
visited = set()
hamiltonian_circuit = []
total_distance = 0
previous_city = 0

for (u, v) in eulerian_circuit:
    if not visited or v == 0:
        hamiltonian_circuit.append(v)
        if len(hamiltonian_circuit) > 1:
            total_distance += distance(hamiltonian_circuit[-2], v)
        visited.add(v)

# Closing the tour by returning to the start point
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)
    total_distance += distance(hamiltonian_circuit[-2], 0)

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_distance, 2))