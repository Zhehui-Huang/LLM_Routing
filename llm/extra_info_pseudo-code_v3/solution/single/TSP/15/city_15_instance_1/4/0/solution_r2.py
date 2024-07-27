import networkx as nx
import math

# Define the coordinates of the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Define a function to calculate Euclidean distance between two points
def euc_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create the graph
G = nx.Graph()

# Add edges between each pair of cities
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euc_dist(cities[i], cities[j]))

# Step 1: Create a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find nodes with an odd degree in T
odd_nodes = [v for v in T.nodes if T.degree(v) % 2 == 1]

# Step 3: Create a subgraph with odd degree nodes
odorphan =nx.Graph.subgraph(G, odd_nodes)
# Find a minimum weight perfect matching (MWP) in the subgraph of the odd degree nodes
odd_matching = nx.algorithms.matching.min_weight_matching(odorphan ,maxcardinality=True,weight='weight')

# Step 4: Add these edges to T
T.add_edges_from(odd_matching)

# Step 5: Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Create the Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the tour cost
tour_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Print results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", tour_cost)