import math
import numpy as np
from itertools import permutations

# Given data for cities and demands
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14,
    10: 8, 11: 7, 12: 14, 13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15
}
robot_capacity = 160
num_robots = 2

# Helper function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create Distance Matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in cities.keys():
    for j in cities.keys():
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Initialize routes for each robot
routes = {k: [[0]] for k in range(num_robots)}

def find_savings():
    savings_list = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                savings = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings_list.append((savings, i, j))
    savings_list.sort(reverse=True, key=lambda x: x[0])
    return savings_list

# Main function to compute routes based on savings
def compute_routes():
    savings_list = find_savings()
    capacity = {k: robot_capacity for k in range(num_robots)}
    for saving, i, j in savings_list:
        # Check if i or j can be added to any existing route
        for k in range(num_robots):
            route = routes[k][0]
            if (demands[i] <= capacity[k]) and (i not in route):
                route.append(i)
                route.append(0)  # Return to depot
                capacity[k] -= demands[i]
                break
            elif (demands[j] <= capacity[k]) and (j not in route):
                route.append(j)
                route.append(0)  # Return to depot
                capacity[k] -= demands[j]
                break

compute_routes()

# Calculate costs for each robot route and total costs
total_cost = 0
for robot_id, robot_routes in routes.items():
    for route in robot_routes:
        route_cost = 0
        for i in range(1, len(route)):
            route_cost += distance_matrix[route[i - 1]][route[i]]
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robot_id} Total Travel Cost: {route_cost}")
        total_cost += route_cost

print(f"Overall Total Travel Cost: {total_cost}")