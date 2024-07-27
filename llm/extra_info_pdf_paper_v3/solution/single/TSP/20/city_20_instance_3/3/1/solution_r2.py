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

# Step 2: Find nodes with odd degree in the MST
odd_degree_nodes = [node for node, degree in MST.degree() if degree % 2 == 1]
odd_subgraph = G.subgraph(odd_degree_nodes)

# Step 3: Find a minimum weight perfect matching in the subgraph of odd degree nodes
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Add matching edges to the MST
MST.add_edges_from(matching)

# Step 4: Create an Eulerian circuit from the augment MST
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Convert the Eulerian circuit to a Hamiltonian path (ignoring repeated visits to nodes)
visited = set()
hamiltonian_circuit = [0]  # Start at the depot

for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

hamiltonian_circuit.append(0)  # Return to the depot to close the tour

# Calculate the total cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Print results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)