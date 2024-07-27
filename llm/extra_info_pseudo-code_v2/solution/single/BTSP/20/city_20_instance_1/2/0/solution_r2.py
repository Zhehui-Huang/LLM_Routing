import math
import networkx as nx

# Define the cities and their coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize the graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Using a simple approximation method like nearest neighbor because TSP is NP-Hard
def nearest_neighbor_tsp(start_node):
    tour = [start_node]
    current_node = start_node
    total_cost = 0
    all_nodes = set(cities.keys())
    unvisited = all_nodes - {start_node}
    
    while unvisited:
        next_node = min(unvisited, key=lambda node: G[current_node][node]['weight'])
        tour.append(next_node)
        total_cost += G[current_node][next_node]['weight']
        current_node = next_node
        unvisited.remove(next_node)
    
    # Return to the starting node
    total_cost += G[tour[-1]][start_node]['weight']
    tour.append(start_node)

    # Get the maximum distance between consecutive cities
    max_distance = max(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Calculate the tour, the total travel cost, and the maximum distance between consecutive cities
tour, total_cost, max_distance = nearest_neighbor_tsp(0)

print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost:.2f}')
print(f'Maximum distance between consecutive cities: {max_distance:.2f}')