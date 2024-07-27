import numpy as np
from math import sqrt
from itertools import combinations

# Given data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

num_cities = len(coordinates)
vehicle_capacity = 160
num_robots = 2

# Compute the Euclidean distance between each pair of cities
def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generate the cost matrix
cost_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            cost_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])
        else:
            cost_matrix[i][j] = float('inf')  # infinite cost to return to the same city

# Calculate savings (Clarke-Wright formula): Sij = C0i + C0j - Cij
saving_matrix = {}
for i, j in combinations(range(1, num_cities), 2):  # start from 1 to exclude the depot
    saving_matrix[(i, j)] = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]

# Sort savings in descending order
sorted_savings = sorted(saving_matrix.keys(), key=lambda x: saving_matrix[x], reverse=True)

# Initialize routes for each vehicle
routes = {k: [[0]] for k in range(num_robots)}

# Assign routes based on savings list
for i, j in sorted_savings:
    assigned = False
    for robot_id, robot_routes in routes.items():
        if assigned:
            break
        for route in robot_routes:
            # Check if it can be appended or prepended in the existing route
            if route[-1] == 0 and sum(demands[route[r]] for r in route) + demands[i] + demands[j] <= vehicle_capacity:
                route.extend([i, j, 0])
                assigned = True
                break
            elif route[0] == 0 and sum(demands[route[r]] for r in route) + demands[i] + demands[j] <= vehicle_capacity:
                route.insert(0, j)
                route.insert(0, i)
                assigned = True
                break

# Calculate the cost of each tour and the overall cost
overall_total_cost = 0
for robot_id, robot_routes in routes.items():
    for route in robot_garage:
        total_cost_route = 0
        last_city = 0
        for city in route[1:]:
            total_cost_route += cost_matrix[last_city][city]
            last_mid = city
        overall_total_cost += total_cost_route
        print(f'Robot {robot_id} Tour: {route}')
        print(f'Robot {robot_id} Total Travel Cost: {total_cost_route}')

print(f'Overall Total Travel Cost: {overall_total_cost}')