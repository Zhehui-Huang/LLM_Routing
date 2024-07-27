import numpy as np

# Define city coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities including depot
n = len(cities)

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create the distance matrix
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Bottleneck TSP Heuristic approach
def bottleneck_tsp(distances):
    visited = np.zeros(n, dtype=bool)
    tour = [0]  # Start at the depot
    visited[0] = True
    total_cost = 0
    max_edge_cost = 0
    
    current_city = 0
    while len(tour) < n:
        nearest = None
        min_dist = float('inf')
        
        for j in range(n):
            if not visited[j] and distances[current_city][j] < min_dist:
                min_dist = distances[current_city][j]
                nearest = j
        
        if nearest is not None:
            tour.append(nearest)
            visited[nearest] = True
            total_cost += min_dist
            max_edge_cost = max(max_edge_cost, min_dist)
            current_city = nearest
    
    # To complete the tour back to the depot
    final_leg_distance = distances[current_city][0]
    tour.append(0)
    total_cost += final_leg_distance
    max_edge_cost = max(max_edge_cost, final_leg_distance)

    return tour, total_cost, max_edge_cost

# Perform the Bottleneck TSP
tour, total_travel_cost, max_distance_between_cities = bottleneck_tsp(distances)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_between_cities)