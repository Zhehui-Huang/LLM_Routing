import numpy as n
import math
from random import shuffle, choice
from itertools import permutations

# Coordinates and demands of cities
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19,
           11, 12, 26, 17, 6, 15]

vehicle_capacity = 160
num_vehicles = 2

# Function to calculate Euclidean distance between two cities
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Creating distance matrix
distance_matrix = []
for i in range(len(coordinates)):
    row = []
    for j in range(len(coordinates)):
        row.append(euclidean_distance(coordinates[i], coordinates[j]))
    distance_matrix.append(row)

# A simple heuristic function to create initial feasible solution: Nearest Neighbor Heuristic
def nearest_neighbor_solution(start_point, demands, capacity, distance_matrix):
    num_cities = len(demands)
    routes = []
    visited = set()
    visited.add(0)
    
    for vehicle in range(num_vehicles):
        route = [start_point]
        current_load = 0
        while len(visited) < num_cities:
            last_city = route[-1]
            next_city = None
            min_distance = float('inf')
            for city in range(num_cities):
                if city not in visited and current_load + demands[city] <= capacity:
                    if distance_matrix[last_city][city] < min_distance:
                        min_distance = distance_matrix[last_city][city]
                        next_city = city
            if next_city is None:  # No city found that can be visited under capacity constraint
                break
            route.append(next_city)
            current_load += demands[next_city]
            visited.add(next_city)
        route.append(start_point)  # Return to depot
        routes.append(route)
        if len(visited) == num_cities:
            break
    
    return routes

# Solve the CVRP
routes = nearest_neighbor_solution(0, demands, vehicle_capacity, distance_matrix)

# Calculate the total travel cost
def calculate_route_cost(route, distance_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    return cost

total_travel_cost = 0
for i, route in enumerate(routes):
    cost = calculate_route_cost(route, distance_matrix)
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Card: {cost}")
    total_travel_code += total_travel_cost
    
print(f"Overall Total Cost: {total_travel_cost}")