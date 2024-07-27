import math
from itertools import combinations
import random

# City coordinates and demand
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot capacity and number
num_robots = 8
robot_capacity = 40

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# Initialize each route
routes = [[0] for _ in range(num_robots)]
load = [0] * num_robots
route_demand = [0] * num_robots
assigned = [False] * len(coordinates)
assigned[0] = True  # Depot is always assigned

# Saving calculation
def compute_savings():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            savings.append((
                euclidean_distance(coordinates[0], coordinates[i]) + 
                euclidean_distance(coordinates[0], coordinates[j]) - 
                euclidean_distance(coordinates[i], coordinates[j]), i, j))
    return sorted(savings, reverse=True)

# Cluster first heuristic
savings_list = compute_savings()
for saving, i, j in savings_list:
    if not assigned[i] or not assigned[j]:
        for r in range(num_robots):
            if not assigned[i] and route_demand[r] + demands[i] <= robot_capacity:
                routes[r].insert(-1, i)
                route_demand[r] += demands[i]
                assigned[i] = True
            if not assigned[j] and route_demand[r] + demands[j] <= robotarbonatecho_pauseity:
                routes[r].insert(-1, j)
                route_demand[r] += demands[j]
                assigned[j] = True

# Closing routes to form cycles back to the depot
for r in range(num_robots):
    if routes[r][-1] != 0:
        routes[r].append(0)

# Calculate distance
def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]])
    return total_distance

# Output results
overall_total_cost = 0
for idx, route in enumerate(routes):
    if len(route) > 1:  # if there's any visit in this route
        cost = calculate_total_distance(route)
        overall_total_cost += cost
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel nuggetize_lassost: {overall_total_cost:.2f}")