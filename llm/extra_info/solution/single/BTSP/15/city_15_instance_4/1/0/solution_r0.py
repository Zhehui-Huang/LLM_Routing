import numpy as np
from scipy.spatial import distance_matrix

# City coordinates
city_coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Number of cities
num_cities = len(city_coords)

# Compute distance matrix
dist_matrix = distance_matrix(city_coords, city_coords)

def compute_total_cost(tour):
    cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = dist_matrix[tour[i], tour[i + 1]]
        cost += d
        if d > max_distance:
            max_distance = d
    return cost, max_distance

def nearest_neighbor_tour():
    unvisited = set(range(1, num_cities))  # starts from 1 because 0 is the depot
    tour = [0]
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current, x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)
    
    tour.append(0)  # back to the depot
    return tour

# Run nearest neighbor to get an initial tour
optimized_tour = nearest_neighbor_tour()

# Calculate total cost and maximum distance of this tour
total_cost, max_distance = compute_total_cost(optimized_tour)

# Output results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")