import numpy as np
import networkx as nx

# Define the city coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Number of cities
n = len(coordinates)

# Function to calculate Euclidean distance
def euclidean_dist(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a complete graph with distances as weights
G = nx.complete_graph(n)
for i in range(n):
    for j in range(i + 1, n):
        G[i][j]['weight'] = euclidean_dist(coordinates[i], coordinates[j])

# Sort edges by weight
edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Use a union-find data structure to help construct a minimum spanning tree
parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Kruskal's algorithm to find Minimum Spanning Tree (MST)
mst = nx.Graph()
for u, v, data in edges:
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        mst.add_edge(u, v, weight=data['weight'])
        parent[root_u] = parent[root_v]
    if mst.number_of_edges() == n-1:
        break

# Double tree method to obtain an approximate tour (creates an Eulerian circuit)
# Duplicate edges in MST (create an undirected multigraph)
dtree = nx.MultiGraph(mst)

# Find an Eulerian circuit in the doubled tree
eulerian_circuit = list(nx.eulerian_circuit(dtree))

# Making the Hamiltonian circuit (visiting each node exactly once)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Complete the tour

# Calculate the total travel cost and maximum distance between consecutive cities
total_cost = 0
max_consecutive_distance = 0
for i in range(len(hamiltonian_circuit) - 1):
    u, v = hamiltonian_circuit[i], hamiltonian_circuit[i + 1]
    dist = G[u][v]['weight']
    total_cost += dist
    max_consecutive_distance = max(max_consecutive high_priority=True)

# Display the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")