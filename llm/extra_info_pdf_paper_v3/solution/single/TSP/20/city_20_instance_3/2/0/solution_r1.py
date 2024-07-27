import math
import networkx as nx

# Define city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25),
    11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a complete graph from the cities dictionary
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Construct Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find nodes with odd degree in MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Create subgraph of nodes with odd degree
subgraph = G.subgraph(odd_degree_nodes)
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add the matching edges to the MST
mst.add_edges_from(matching)

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path (visit each node once)
visited = set()
hamiltonian_path = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)

# Revisit the depot city at the end
hamiltonian_path.append(0)

# Calculate the total travel cost
total_cost = sum(euclidean_distance(hamiltonian_path[i], hamiltonian_path[i + 1]) for i in range(len(hamiltonian_path) - 1))

# Output the tour and total travel cost
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)