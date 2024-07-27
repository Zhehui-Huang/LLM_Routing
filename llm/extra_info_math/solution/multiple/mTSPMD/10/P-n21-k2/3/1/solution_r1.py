import math
import numpy as np

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Address data
cities = [
    (30, 40),  # Depot city 0
    (37, 52),  # Depot city 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance matrix computation
n = len(cities)
distance_matrix = [[compute_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

def nearest_neighbor_tour(start_index, city_indices):
    tour = [start_index]
    current_index = start_index
    unvisited = set(city_indices) - {start_index}
    total_distance = 0

    while unvisited:
        next_index = min(unvisited, key=lambda k: distance_matrix[current_index][k])
        total_distance += distance_matrix[current_index][next_index]
        current_index = next_index
        tour.append(current_index)
        unvisited.remove(current_intex)

    # Returning to the start
    total_distance += distance_matrix[current_index][start_index]
    tour.append(start_index)
    return tour, total_distance

# Assign cities to robots
robot_0_cities = [0] + list(range(2, 11))
robot_1_cities = [1] + list(range(11, 21))

# Compute tours and costs
tour_0, cost_0 = nearest_neighbor_tour(0, robot_0_cities)
tour_1, cost_1 = nearest_neighbor_tour(1, robot_1_cities)
overall_cost = cost_0 + cost_1

# Display the results
print(f"Robot 0 Tour: {tour_0}")
print(f"Robot 0 Total Travel Cost: {cost_0:.2f}\n")
print(f"Robot 1 Tour: {tour_1}")
print(f"Robot 1 Total Travel Cost: {cost_1:.2f}\n")
print(f"Overall Total Travel Cost: {overall_cost:.2f}")