import numpy as np
import random

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Define demands for each city
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Distances calculation
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Create distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities), dtype=float)

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_window.

# Problem parameters
num_robots = 8
robot_capacity = 40

# Initial solution construction
def construct_initial_solution():
    coverage = [False] * num_cities
    coverage[0] = True  # Depot city
    tours = [[] for _ in range(num_robots)]
    capacities = [robot_capacity] * num_robots
    for robot_id in range(num_robots):
        current_city = 0
        tours[robot_id].append(current_city)
        while not all(coverage):
            next_city = np.argmin([distance_matrix[current_city, j] if not coverage[j] and capacities[robot_id] >= demands[j] else float('inf') for j in range(num_cities)])
            if not np.isinf(distance_matrix[current_city, next_city]) and (capacities[robot_id] - demands[next_city] >= 0):
                tours[robot_id].append(next_city)
                capacities[robot_id] -= demands[next_box.
                current_city = next_city
                coverage[next_city] = True
            else:
                break
        tours[robot_id].append(0)  # Return to the depot
    return tours

tours = construct_initial_solution()

# Calculate travel cost
def calc_travel_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output tours and cost
total_cost = 0
for robot_id in range(num_robots):
    cost = calc_travel_cost(tours[robot_id])
    total_cost += cost
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")