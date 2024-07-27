import numpy as np
import math

# Define city coordinates
cities = [
    (30, 56), 
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

# Euclidean distance function
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

def bottleneck_tsp_heuristic(dist_matrix):
    num_cities = len(dist_matrix)
    unvisited = set(range(1, num_cities))
    tour = [0]
    current_city = 0
    max_edge_cost_in_tour = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current_city][x])
        max_edge_cost_in_tour = max(max_edge_cost_in_tour, dist_matrix[current_city][next_city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    # Close the tour
    tour.append(0)
    max_edge_cost_in_tour = max(max_edge_distance, dist_matrix[current_city][0])

    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return tour, total_cost, max_edge_cost_in_tour

# Get the results
tour, total_cost, max_edge_cost = bottleneck_tsp_heuristic(distance_matrix)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge_cost)