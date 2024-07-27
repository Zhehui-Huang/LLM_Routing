import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean
from random import random, randint, shuffle

# Define cities' coordinates
cities_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of robots and their capacities
num_robots = 8
robot_capacity = 35

# Function to compute the Euclidean distance matrix
def compute_cost_matrix(coords):
    num_cities = len(coords)
    cost_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                cost_matrix[i][j] = euclidean(coords[i], coords[j])
            else:
                cost_matrix[i][j] = float('inf')  # No self-loops
    return cost_matrix

# Clarke-Wright Savings Algorithm Initial Setup
def calculate_savings(cost_matrix):
    num_cities = len(cost_matrix)
    savings_list = []
    for i in range(1, num_cities):     # Start from 1 to skip depot city 0
        for j in range(1, num_cities):
            if i != j:
                saving = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings_list.append((saving, i, j))
    # Sort savings in descending order
    savings_list.sort(reverse=True, key=lambda x: x[0])
    return savings_list

# Creating initial feasible solutions
def initial_solution(savings, demands, capacity):
    routes = []
    demand_fulfilled = [False] * len(demands)
    demand_fulfilled[0] = True  # Depot does not need to be fulfilled
    for _, i, j in savings:
        if not demand_fulfilled[i] and not demand_fulfilled[j]:
            if demands[i] + demands[j] <= capacity:
                routes.append([0, i, j, 0])
                demand_fulfilled[i] = True
                demand_fulfilled[j] = True
    
    # Add remaining unfulfilled demands
    for i, fulfilled in enumerate(demand_fulfilled):
        if not fulfilled:
            if demands[i] <= capacity:
                routes.append([0, i, 0])
                demand_fulfilled[i] = True

    return routes

# Compute the total travel cost of a route
def calculate_route_cost(route, cost_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += cost_matrix[route[i]][route[i + 1]]
    return cost

# Compute solution
cost_matrix = compute_cost_matrix(cities_coords)
savings = calculate_savings(cost_matrix)
routes = initial_solution(savings, demands, robot_capacity)
total_cost = 0

for idx, route in enumerate(routes):
    route_cost = calculate_route_cost(route, cost_matrix)
    total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")