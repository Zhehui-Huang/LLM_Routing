import math
import networkx as nx

def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Specifying positions for the depot and the cities
cities_positions = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Creating a complete graph
G = nx.Graph()
number_of_cities = len(cities_positions)

for i in range(number_of_cities):
    for j in range(i + 1, number_of_cities):
        G.add_edge(i, j, weight=euclidean_distance(cities_positions[i], cities_positions[j]))

# Implementing Christofides Algorithm
# Step 1: Minimum Spanning Tree
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Vertices of odd degree
odd_degree_nodes = [v for v in T.nodes if T.degree(v) % 2 != 0]

# Step 3: Minimum weight perfect matching
min_weight_matching = nx.Graph()
min_weight_matching.add_nodes_from(odd_degree_nodes)

# Using a lazy approach for perfect matching for simplicity
for node in odd_degree_nodes:
    distances = {neighbor: euclidean_distance(cities_positions[node], cities_positions[neighbor]) for neighbor in odd_degree_nodes if neighbor != node}
    min_neighbor = min(distances, key=distances.get)
    min_weight_matching.add_edge(node, min_neighbor, weight=distances[min_neighbor])

# Step 4: Combine edges of MST and the matching to create a multigraph
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching.edges(data=True))

# Step 5: Find the Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Create Hamiltonian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = []

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)  # Returning to the depot city

# Calculate total tour cost
total_cost = sum(euclidean_distance(cities_positions[hamiltonian_circuit[i]], cities_positions[hamiltonian_circuit[i+1]]) for i in range(len(hamiltonian_circuit)-1))

# Display the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))