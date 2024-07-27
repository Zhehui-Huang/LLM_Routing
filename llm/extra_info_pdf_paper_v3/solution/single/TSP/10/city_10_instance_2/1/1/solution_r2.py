import numpy as np
from math import sqrt

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Create the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Nearest Neighbor TSP Algorithm
def nearest_neighbor_tsp(dist_matrix, start_city):
    num_cities = len(dist_matrix)
    visited = [False] * num_cities
    tour = [start_city]
    current_city = start_city
    visited[current_city] = True
    total_cost = 0

    for _ in range(1, num_cities):
        next_city = None
        min_dist = float('inf')
        for city in range(num_cities):
            if not visited[city] and dist_matrix[current_city][city] < min_dist:
                min_dist = dist_matrix[current_city][city]
                next_city = city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        current_city = next_city
    
    # Return to the start city
    total_cost += dist_matrix[current_city][start_city]
    tour.append(start_city)
    
    return tour, total_cost

# Solve the TSP
tour, total_cost = nearest_neighbor_tsp(distance_matrix, 0)

# Output the tour and the total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)