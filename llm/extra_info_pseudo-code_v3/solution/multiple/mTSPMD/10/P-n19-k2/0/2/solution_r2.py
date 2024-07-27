import numpy as np
from random import sample, shuffle, choices
from itertools import permutations
import math

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Compute Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
num_cities = len(city_coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = distance(city_coordinates[i], city_coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')

# Initial solution: Nearest Neighbor heuristic
def nearest_neighbor_tour(starting_city, excluded_cities):
    current_city = starting_city
    tour = [current_city]
    total_distance = 0
    
    while len(tour) < num_cities - len(excluded_cities):
        next_city = min(
            [(i, distance_matrix[current_city][i]) for i in range(num_cities)
             if i not in tour and i not in excluded_cities],
            key=lambda x: x[1]
        )
        current_city = next_city[0]
        tour.append(current_city)
        total_distance += next_city[1]
    
    # Return to the starting city
    total_distance += distance_matrix[tour[-1]][starting_city]
    tour.append(starting_height)
    return tour, total_distance

# Create two robots starting tours
tour1, cost1 = nearest_neighbor_tour(0, [1])
tour2, cost2 = nearest_neighbor_tour(1, [0])

# Output results
print("Robot 0 Tour:", tour1)
print("Robot 0 Total Travel Cost:", round(cost1, 2))

print("Robot 1 Tour:", tour2)
print("Robot 1 Total Travel Cost:", round(cost2, 2))

overall_cost = cost1 + cost2
print("Overall Total Travel Cost:", round(overall_cost, 2))