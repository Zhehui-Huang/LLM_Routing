import math
import networkx as nx

# Define the cities and their coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Create a complete graph with Euclidean distances as edge weights
G = nx.Graph()
for i, coord1 in enumerate(coordinates):
    for j, coord2 in enumerate(coordinates):
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(coord1, coord2))

# Using minimum spanning tree to approximate Biconnected subgraph
mst = nx.minimum_spanning_tree(G)

# Make the tree biconnected
# Add one extra edge to make the graph biconnected in a simple way
edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
for edge in edges_sorted_by_weight:
    if not mst.has_edge(edge[0], edge[1]):
        mst.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(mst):
            break

# Extract a tour from the approximate biconnected graph using a TSP approach (Christofides algorithm)
# For simplicity, we will use a straightforward heuristic:
# Start from the depot, select the closest unvisited city sequentially
def tsp_heuristic(G, start_node):
    tour = [start_node]
    current_node = start_node
    nodes_set = set(G.nodes())
    remaining_nodes = nodes_set - {start_node}
    
    while remaining met:
        next_node = min(remaining_nodes, key=lambda node: G[current_node][node]['weight'])
        tour.append(next_node)
        remaining_nodes.remove(next_node)
        current_node = next_node
    
    tour.append(start_node)  # to return to the depot at the end
    return tour

# Get the tour
tour = tsp_heuristic(mst, 0)

# Calculate the costs
total_travel_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
max_distance_between_cities = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_between_cities)