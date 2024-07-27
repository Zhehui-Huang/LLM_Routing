import math
import numpy as np

# Constants
NUMBER_OF_ROBOTS = 4
ROBOT_CAPACITY = 6000

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 
    400, 800, 100, 500, 600, 1200, 
    1300, 1300, 300, 900, 2100, 1000, 
    900, 2500, 1800, 700
]

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def construct_cost_matrix(coords):
    n = len(coords)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                cost_matrix[i][j] = calculate_distance(coords[i], coords[j])
    return cost_matrix

def calculate_savings_matrix(cost_matrix):
    n = len(cost_matrix)
    savings_matrix = np.zeros((n, n))
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                savings_matrix[i][j] = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
    return savings_matrix

def solve_cvrp(cost_matrix, demands, vehicle_capacity):
    n = len(demands)
    routes = []
    capacities = [vehicle_capacity] * NUMBER_OF_ROBOTS
    assigned = [False] * n

    while not all(assigned[1:]):
        route = [0]
        load = 0
        for i in range(1, n):
            if not assigned[i] and load + demands[i] <= vehicle_capacity:
                load += demands[i]
                assigned[i] = True
                route.append(i)
        route.append(0)
        routes.append(route)
        capacities.append(load)
    
    return routes

def print_solution(routes, cost_matrix):
    total_cost = 0
    for idx, route in enumerate(routes):
        cost = sum(cost_mkatrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {cost}")
        total_cost += cost
    print(f"Overall Total Travel Cost: {total_cost}")

# Main execution begins
cost_matrix = construct_cost_matrix(coordinates)
savings_matrix = calculate_savings_matrix(cost_matrix)
routes = solve_cvrp(cost_matrix, demands, ROBOT_CAPACITY)
print_solution(routes, cost_matrix)