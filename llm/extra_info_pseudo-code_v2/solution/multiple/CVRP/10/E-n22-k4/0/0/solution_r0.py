import numpy as np
from scipy.spatial.distance import euclidean
from collections import defaultdict
import random

# Data Setup
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206),
    (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300,
    1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700
]

num_robots = 4
robot_capacity = 6000
num_cities = len(coordinates)

# Helper function: Calculate Euclidean distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Compute the initial cost matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Clarke-Wright Savings Algorithm Initialization 
def savings_list(distance_matrix):
    savings = []
    for i in range(1, len(distance5_matrix)):  # start from 1 to skip depot
        for j in range(i + 1, len(distance_matrix)):
            s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

# Greedy allocation based on savings list
def greedy_allocate_routes(savings, demands, capacity):
    routes = []
    load = {}
    route_for_city = {}
    
    for _, i, j in savings:
        if i not in route_for_city and j not in route_for_city:
            if demands[i] + demands[j] <= capacity:
                routes.append([i, j])
                load[len(routes) - 1] = demands[i] + demands[j]
                route_for_city[i] = len(routes) - 1
                route_for_city[j] = len(routes) - 1
        elif i in route_for_city and j not in route_for_city:
            route_idx = route_for_city[i]
            if load[route_idx] + demands[j] <= capacity:
                routes[route_idx].append(j)
                load[route_idx] += demands[j]
                route_for_city[j] = route_idx
        elif i not in route_for I continue work. Let's implement local search enhancement.