import math
import networkx as nx

# Define the cities and their coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Initialize a complete graph
G = nx.Graph()
for i, pos1 in enumerate(coordinates):
    for j, pos2 in enumerate(coordinates):
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(pos1, pos2))

# Applying Prim's algorithm to find the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Function to ensure the graph is biconnected by adding minimum needed edges
def make_biconnected(G):
    if nx.is_biconnected(G):
        return G
    components = list(nx.biconnected_components(G))
    # Articulation points would need extra edges to be involved in a cycle
    articulation_points = list(nx.articulation_points(G))
    # (Optional) Heuristic to minimize the number of bridges/edges needed
    biconnected_graph = G.copy()
    while not nx.is_biconnected(biconnected_graph):
        for u, v in articulation_points:
            for target in set(G.nodes()) - {u, v}:
                if not biconnected_graph.has_edge(u, target):
                    biconnected_graph.add_edge(u, target, weight=G[u][target]['weight'])
                    break
            if nx.is_biconnected(biconnected_graph):
                break
    return biconnected_graph

biconnected_mst = make_biconnected(mst)

# Find an Eulerian tour (Hierarchy, insure Hamiltonian by shortcutting)
def find_eulerian_tour(G, start=0):
    eulerian_tour = list(nx.eulerian_circuit(G, source=start))
    visited = set()
    path = [start]
    for u, v in eulerian_tour:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(start)  # Complete tour by returning to start
    return path

tour = find_eulerian_tour(biconnected_mst)

total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)