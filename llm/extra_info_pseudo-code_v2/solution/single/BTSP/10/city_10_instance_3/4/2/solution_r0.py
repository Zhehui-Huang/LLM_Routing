import math
import networkx as nx

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate the complete graph with edge weights
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.edges[i, j]['weight'] = euclidean_distance(cities[i], cities[j])

# Step 1: Apply Algorithm BB
# Sort the edges in non-decreasing order of their weights
edges_sorted = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
E_BB = []

# Initialize Union-Find to check for biconnected components
uf = nx.utils.union_find.UnionFind()

# Augmentation step
for edge in edges_sorted:
    u, v, data = edge
    if uf[u] != uf[v]:
        E_BB.append(edge)
        uf.union(u, v)
        # Check if G(V, E_BB) is biconnected
        G_BB = nx.Graph()
        G_BB.add_nodes_from(G.nodes())
        G_BB.add_edges_from((e[0], e[1]) for e in E_BB)
        if nx.is_biconnected(G_BB):
            break

# Step 2: Tour Identification
# Reconstruct the subgraph from E_BB
G_BB = nx.Graph()
G_BB.add_nodes_from(G.nodes())
G_BB.add_edges_from((e[0], e[1]) for e in E_BB)

# Using a simple nearest neighbor heuristic to find the Hamiltonian cycle in the reduced graph
def nearest_neighbor_tsp(start_node):
    visited = {start_node}
    path = [start_node]
    current_node = start_node
    while len(visited) < len(G_BB.nodes()):
        neighbors = [(n, G_BB[current_node][n]['weight']) for n in G_BB.neighbors(current_node)]
        next_node = min((n for n in neighbors if n[0] not in visited), key=lambda x: x[1])[0]
        path.append(next_node)
        visited.add(next_node)
        current_node = next_node
    path.append(start_node)  # complete the cycle
    return path

tour = nearest_neighbor_tsp(0)

# Calculate tour cost and maximum edge cost
tour_cost = sum(G.edges[tour[i], tour[i + 1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(G.edges[tour[i], tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", tour_cost)
print("Maximum distance between consecutive cities:", max_distance)