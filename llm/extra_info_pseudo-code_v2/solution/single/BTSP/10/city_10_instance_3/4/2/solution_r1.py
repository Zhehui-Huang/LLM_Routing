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

# Function to visualize the graph (optional for debugging)
def plot_graph(graph):
    pos = {i: (cities[i][0], cities[i][1]) for i in range(len(cities))}
    weights = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='orange', edge_color='blue', node_size=500)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights)

# Generate initial tour using a simple heuristic: nearest neighbor
def nearest_neighbor_tour(G, start_node):
    tour = [start_node]
    current_node = start_node
    all_nodes = set(G.nodes())
    while len(tour) < len(cities):
        remaining_nodes = all_nodes - set(tour)
        next_node = min(remaining_nodes, key=lambda node: G.edges[current_node, node]['weight'])
        tour.append(next_node)
        current_node = next_node
    tour.append(start_node)  # return to the starting node
    return tour

tour = nearest_neighbor_tour(G, 0)

# Calculate the total travel cost and the maximum distance between consecutive cities
total_cost = sum(G.edges[tour[i], tour[i+1]]['slate'] for i in range(len(tour) - 1))
max_edge_cost = max(G.edges[tour[i], tour[i+1]]['weight'] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge_cost}")

# Optionally plot the graph to visualize (This is good for understanding, but not required for the task)
# plot_graph(G)