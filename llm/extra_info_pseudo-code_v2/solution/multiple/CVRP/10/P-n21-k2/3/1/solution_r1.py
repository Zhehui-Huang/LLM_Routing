import numpy as np
from math import sqrt
from itertools import combinations

# Environment information
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15
]

# Constants
num_cities = len(coordinates)
vehicle_capacity = 160
num_robots = 2

# Helper functions
def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix
cost_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Calculate savings
savings = {}
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        savings[(i, j)] = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]

# Sort savings
sorted_savings = sorted(savings.items(), key=lambda item: -item[1])

# Initialize routes
routes = {k: [] for k in range(num_robots)}
current_load = {k: 0 for k in range(num_robots)}

# Constructing initial feasible solution
for (i, j), saving in sorted_savings:
    if demands[i] + demands[j] > vehicle_capacity:
        continue
    
    assigned = False
    for k in range(num_robots):
        if current_load[k] + demands[i] + demands[j] <= vehicle_capacity:
            routes[k].append([0, i, j, 0])
            current_load[k] += demands[i] + demands[j]
            assigned = True
            break
    
    if not assigned:
        for k in range(num_robots):
            for route in routes[k]:
                if route[-2] == i and current_load[k] + demands[j] <= vehicle_capacity:
                    route.insert(-1, j)
                    current_load[k] += demands[j]
                    assigned = True
                    break
                elif route[1] == j and current_load[k] + demands[i] <= vehicle_capacity:
                    route.insert(1, i)
                    current_load[k] += demands[i]
                    assigned = True
                    break
            if assigned:
                break

# Calculate route costs
overall_total_cost = 0
for robot_id, robot_routes in routes.items():
    for route in robot_routes:
        route_cost = 0
        for idx in range(len(route) - 1):
            route_cost += cost_matrix[route[idx]][route[idx + 1]]
        overall_total_cost += route_cost
        print(f'Robot {robot_id} Tour: {route}')
        print(f'Robot {robot_id} Total Travel Cost: {route_cost}')

print(f'Overall Total Travel Cost: {overall_total_cost}')