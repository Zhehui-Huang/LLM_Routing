import math
import numpy as np

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Building the distance matrix
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i, j] = float('inf')

# Simple heuristic: Nearest Neighbor approach adapted to minimize the bottleneck
def nearest_neighbor_btsp(start=0):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current, x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # Complete the tour by returning to the start
    return tour

# Calculate tour using heuristic
tour = nearest_neighbor_btsp()

# Calculate total distance and maximum step distance in tour
total_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    step_distance = distance_matrix[tour[i-1], tour[i]]
    total_cost += step_distance
    if step_distance > max_distance:
        max_distance = step_distance

# Print the output in the required format
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)