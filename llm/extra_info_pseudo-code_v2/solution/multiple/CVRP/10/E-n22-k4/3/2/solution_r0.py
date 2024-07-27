import math
import numpy as np
from random import randint, random, shuffle

# Coordinates and demands of the cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700
]
num_cities = len(coordinates)
robot_capacity = 6000

# Calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate cost matrix
def create_cost_matrix():
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
    return matrix

cost_matrix = create_cost_matrix()

# Workspace for robots
routes = [[] for _ in range(4)]
capacities = [0] * 4
costs = [0] * 4

def calculate_savings():
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

savings = calculate_savings()

# CW algorithm to assign routes
for saving in savings:
    _, i, j = saving
    in_route_i = in_route_j = None
    for idx in range(4):
        if i in routes[idx]:
            in_route_i = idx
        if j in routes[idx]:
            in_route_j = idx
    if in_route_i is not None and in_route_j is not None:
        continue
    if in_route_i is not None and capacities[in_route_i] + demands[j] <= robot_capacity:
        routes[in_route_i].append(j)
        capacities[in_route_i] += demands[j]
        costs[in_route_i] += cost_matrix[routes[in_route_i][-2]][j]
    elif in_route_j is not None and capacities[in_route_j] + demands[i] <= robot_capacity:
        routes[in_route_j].append(i)
        capacities[in_route_j] += demands[i]
        costs[in_route_j] += cost_matrix[routes[in_route_j][-2]][i]
    elif in_route_i is None and in_route_j is None:
        for idx in range(4):
            if capacities[idx] + demands[i] + demands[j] <= robot_capacity:
                routes[idx].extend([i, j])
                capacities[idx] += (demands[i] + demands[j])
                costs[idx] += (cost_matrix[0][i] + cost_matrix[i][j])
                break

# Close routes
for idx in range(4):
    if routes[idx]:
        costs[idx] += cost_matrix[routes[idx][-1]][0]
        routes[idx] = [0] + routes[idx] + [0]

# Output the results
overall_cost = sum(costs)
for idx in range(4):
    if routes[idx]:
        print(f"Robot {idx} Tour: {routes[idx]}")
        print(f"Robot {idx} Total Travel Cost: {costs[idx]}")
print(f"Overall Total Travel Cost: {overall_cost}")