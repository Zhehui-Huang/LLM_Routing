import numpy as np
import random

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Demand for each city
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot information
num_robots = 4
robot_capacity = 6000
depot = 0

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

def calculate_cost_matrix(coords):
    num_cities = len(coords)
    cost_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            cost_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return cost_matrix

def calculate_savings(cost_matrix, depot):
    num_cities = len(cost_matrix)
    savings = []
    for i in range(num_cities):
        if i == depot:
            continue
        for j in range(i+1, num_cities):
            if j == depot:
                continue
            savings.append((i, j, cost_matrix[depot][i] + cost_matrix[depot][j] - cost_matrix[i][j]))
    return sorted(savings, key=lambda x: x[2], reverse=True)

def initialize_routes(savings, demands, capacity):
    routes = []
    capacities = []
    used = set([depot])
    for saving in savings:
        i, j, _ = saving
        if i in used and j in used:
            continue
        if demands[i] + demands[j] > capacity:
            continue
        route = [depot, i, j, depot]
        routes.append(route)
        capacities.append(demands[i] + demands[j])
        used.update([i, j])
    return routes, capacities

cost_matrix = calculate_cost_matrix(coordinates)
savings = calculate_savings(cost_matrix, depot)
initial_routes, initial_capacities = initialize_routes(savings, demands, robot_capacity)

# Placeholder to add more code for iterative improvement and route post-improvement