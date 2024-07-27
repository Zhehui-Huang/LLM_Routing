import math
import networkx as nx
from heapq import heappop, heappush

# Define cities with their coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate the Euclidean distance between two cities
def dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Create the graph for the cities
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=dist(i, j))

# Function to find the minimum bottleneck spanning tree using Kruskal's algorithm with a slight modification to maximize biconnectivity
def minimum_bottleneck_spanning_tree(G):
    edges = list(G.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])
    forest = nx.Graph()
    forest.add_nodes_from(G.nodes())
    num_components = len(G.nodes())
    mst_edges = []

    # Union-find structures to handle cycle detection and component management
    parent = {node: node for node in G.nodes()}
    rank = {node: 0 for node in G.nodes()}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])  # Path compression
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True
        return False

    # Kruskal's algorithm to add edges ensuring no cycles
    for u, v, data in edges:
        if union(u, v):
            forest.add_edge(u, v, weight=data['weight'])
            mst_edges.append((u, v, data['weight']))
            num_components -= 1
            if num_components == 1:
                break
    
    return forest, mst_edges

# Getting Minimum Bottleneck Spanning Tree
mbst, mbst_edges = minimum_bottleneck_spanning_tree(G)

# Using the Yen's algorithm helpers to create superior paths in the graph for Hamilton cycle completion
def valid_tour(cycle):
    return len(set(cycle)) == len(G.nodes()) and len(cycle) == len(G.nodes()) + 1 and cycle[0] == cycle[-1]

# Attempt to convert mst to a Hamiltonian cycle that starts and ends at the depot 0
def find_hamiltonian_cycle(mbst, start_node=0):
    path = list(nx.dfs_preorder_nodes(mbst, source=start_node))
    path.append(start_node)
    
    if valid_tour(path):
        return path
    else:
        # Repeated visits eliminated by shortcutting; not perfect, used heuristic for shortening
        seen = set()
        cycle = []
        for node in path:
            if node not in seen:
                seen.add(node)
                cycle.append(node)
        cycle.append(start_node)
        return cycle

# Generate the Hamiltonian cycle
hamiltonian_cycle = find_hamiltonian_cycle(mbst, start_node=0)

# Calculate max distance and total travel cost
max_distance = 0
total_cost = 0
for i in range(1, len(hamiltonian_cycle)):
    curr_dist = dist(hamiltonian_cycle[i-1], hamiltonian_cycle[i])
    total_cost += curr_dist
    if curr_dist > max_distance:
        max_distance = curr_dist

# Print results
print(f"Tour: {hamiltonpop()}iltonian_cycle}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")