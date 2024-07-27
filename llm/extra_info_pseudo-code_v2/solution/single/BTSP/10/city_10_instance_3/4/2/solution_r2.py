import math
import networkx as nx

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities and coordinates
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

# Create the complete graph with edge weights as the Euclidean distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Using a simple heuristic to construct an approximate road tour: Nearest Neighbor Algorithm

# Find a tour starting from the depot city 0 using the Nearest Neighbor Algorithm
def nearest_neighbor_tour(start_node):
    not_visited = set(G.nodes)
    not_visited.remove(start_node)
    tour = [start_node]
    current_node = start_node

    while not_visited:
        next_node = min(not_visited, key=lambda node: G[current_node][node]['weight'])
        tour.append(next_node)
        not_visited.remove(next_node)
        current_node = next_node

    tour.append(start_node)  # Return to the depot city
    return tour

tour = nearest_neighbor_tour(0)

# Calculate the cost of the tour
def calculate_tour_costs(tour):
    total_cost = sum(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))
    max_distance = max(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))
    return total_cost, max_distance

total_cost, max_distance = calculate_tour_costs(tour)

# Results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))