import numpy as np
import random

# Data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63),
               (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40
num_robots = 8

num_cities = len(coordinates)

# Compute distance matrix
def euclidean(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distance_matrix = [[euclidean(coordinates[i], coordinates[j]) for j in range(num_cents)] for i in range(num_hubs)]

# Initialize savings list
savings = []
for i in range(1, num_hubs):
    for j in range(i + 1, num_cities):
        s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
        savings.append((s, i, j))
savings.sort(reverse=True, key=lambda x: x[0])  # Sort by savings in descending order

# Initial route construction
routes = []
capacity_used = [0] * num_robots
current_robot = 0

for s, i, j in savings:
    if current_robot < num_robots and (capacity_used[current_robot] + demands[i] + demands[j]) <= robot_capacity:
        routes.append([0, i, j, 0])
        capacity_used[current_robot] += (demands[i] + demands[j])
        current_robot += 1

# Post-improvement process: Try to optimize further here based on the paper's guidelines

# Calculate travel costs
def calculate_route_cost(route):
    return sum([distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)])

costs = [calculate_route_cost(route) for route in routes]
overall_total_cost = sum(costs)

# Output results
for i, route in enumerate(routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")