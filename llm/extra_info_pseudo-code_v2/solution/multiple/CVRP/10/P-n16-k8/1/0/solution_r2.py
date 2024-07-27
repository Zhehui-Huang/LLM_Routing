import numpy as np
import math

# Data about cities and their demands
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot properties
num_robots = 8
capacity = 35

# Helper function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a distance matrix
n = len(cities_coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities_coordinates[i], cities_coordinates[j])

# Clarke-Wright Savings Algorithm
def calculate_savings():
    savings = []
    for i in range(1, n):
        for j in range(i+1, n):
            if i != j:
                s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

savings = calculate_savings()

# Apply Clarke-Wright to initialize routes
routes = []
loads = {}

for _, i, j in savings:
    if demands[i] + demands[j] <= capacity:
        # Try to merge nodes in new or existing routes
        found = False
        for route in routes:
            if route[0] == i and demands[j] + loads[route[-1]] <= capacity:
                route.insert(0, j)
                loads[route[-1]] += demands[j]
                found = True
                break
            elif route[-1] == j and demands[i] + loads[route[0]] <= capacity:
                route.append(i)
                loads[route[0]] += demands[i]
                found = True
                break
        if not found:
            routes.append([i, j])
            loads[(i, j)] = demands[i] + demands[j]  # start tracking load of this route

# Ensure starting at depot
final_routes = [[0] + route + [0] for route in routes]

# Robot assignment to balance load
robot_assignments = [[] for _ in range(num_robots)]
robot_load = [0] * num_robots
for route in final_intra_routes:
    # naive assignment to balance robot load
    min_index = np.argmin(robot_loads)
    robot_assignments[min_index].append(route)
    robot_load[min_index] += sum(demands[city] for city in route)

# Output the results
overall_cost = 0
for index, routes in enumerate(robot_assignments):
    print(f"Robot {index} Tours:")
    for route in routes:
        route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        print(f"  {route} with travel cost {route_cost:.2f}")
        overall_cost += route_cost
    print()

print(f"Overall Total Travel Cost: {overall_cost:.2 wnds f}")