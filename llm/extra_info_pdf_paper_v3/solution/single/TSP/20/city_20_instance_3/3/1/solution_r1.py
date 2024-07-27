import math
import networkx as nx

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.Graph()

# Add nodes and edges with distances
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        dist = euclidean_distance(cities[i], cities[j])
        G.add_edge(i, j, weight=dist)

# Step 1: Create a minimum spanning tree
MST = nx.minimum_spanning_tree(G)

# Step 2: Create a subgraph from nodes with odd degree
odd_degree_nodes = [node for node, degree in dict(MST.degree()).items() if degree % 2 == 1]
odd_subgraph = G.subgraph(odd_degree_nodes)

# Step 3: Find a minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Add matching edges to the MST to create an Eulerian graph
MST.add_edges_from(matching)

# Step 4: Create an Eulerian tour
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Step 5: Convert Eulerian tour to Hamiltonian circuit
# Hamiltonian circuit should visit each node exactly once.
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Return to the starting point

# Calculate the total cost of the Hamiltonian circuit
total_cost = 0
for i in range(len(hamiltonian_circuit) - 1):
    edge_weight = G.get_edge_data(hamiltonian_circuit[i], hamiltonian_circuit[i + 1])['weight']
    total_cost += edge_weight

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)