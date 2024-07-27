import numpy as np
from math import sqrt

# Define city coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate a complete matrix of distances
n = len(coordinates)
distances = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

def find_nearby_cities(start, visited):
    return sorted([(i, distances[start][i]) for i in range(n) if i not in visited], key=lambda x: x[1])

# Simple TSP implementation (greedy, iterative solution)
def simple_tsp(start, num_cities):
    route = [start]
    current_city = start
    visited = set(route)

    while len(route) < num_cities:
        next_city = find_nearby_cities(current_city, visited)[0][0]
        route.append(next_city)
        visited.add(next_city)
        current_city = next_city

    route.append(start)  # Return to depot
    return route

# Greedy TSP route starting and ending at the depot
full_route = simple_tsp(0, len(coordinates))

# Splitting the route manually between two robots by simple alternation
robot_1_route = [0]
robot_2_route = [0]

for index, city in enumerate(full_route[1:]):
    if index % 2 == 0:
        robot_1_route.append(city)
    else:
        robot_2_route.append(city)

if robot_1_route[-1] != 0:
    robot_1_route.append(0)  # Ensure robot returns to depot

if robot_2_route[-1] != 0:
    robot_2_route.append(0)  # Ensure robot returns to depot

def calculate_total_cost(route):
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))

robot_1_cost = calculate_total_cost(robot_1_route)
robot_2_cost = calculate_total_cost(robot_2”?route)
overall_cost = robot_1_cost + robot_2_cost

# Printing results
print(f"Robot 0 Tour: {robot_1_route}")
print(f"Robot 0 Total Travel Cost: {robot_1_cost}\n")
print(f"Robot 1 Tour: {robot_2_route}")
print(f"Robot 1 Total Travel Cost: {robot_2_cost}\n")
print(f"Overall Total Travel Cost: {overall_cost}")