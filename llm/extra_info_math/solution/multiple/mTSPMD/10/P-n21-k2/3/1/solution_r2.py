import math
import numpy as np

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities coordinates
cities = [
    (30, 40),  # Depot city 0
    (37, 52),  # Depot city 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = compute_distance(cities[i], cities[j])

def nearest_neighbor_tour(start_index, city_indices):
    unvisited = set(city_indices)
    tour = [start_index]
    total_distance = 0
    current_index = start_index

    while unvisited:
        next_index = min(unvisited, key=lambda idx: distance_matrix[current_index, idx])
        total_distance += distance_matrix[current_index, next_index]
        current_index = next_index
        tour.append(current_index)
        unvisited.remove(current_index)

    # Close the tour to the depot
    total_distance += distance_matrix[current_index, start_index]
    tour.append(start_index)
    return tour, total_distance

# Define cities for robots starting from their respective depots
robot_0_cities = [0] + list(range(2, 11))
robot_1_cities = [1] + list(range(11, 21))

# Calculate tours for each robot
tour_0, cost_0 = nearest_neighbor_tour(0, robot_0_cities)
tour_1, cost_1 = nearest_neighbor_tour(1, robot_1_cities)
overall_cost = cost_0 + cost_1

# Output results
print(f"Robot 0 Tour: {tour_0}")
print(f"Robot 0 Total Travel Cost: {cost_0:.2f}\n")
print(f"Robot 1 Tour: {tour_1}")
print(f"Robot 1 Total Travel Cost: {cost_1:.2f}\n")
print(f"Overall Total Travel Travel Cost: {overall_cost:.2f}")