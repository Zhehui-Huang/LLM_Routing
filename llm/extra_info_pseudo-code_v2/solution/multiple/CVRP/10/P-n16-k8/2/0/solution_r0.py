import numpy as np
from scipy.spatial.distance import euclidean
from random import randint, random, shuffle

# City coordinates and demand list
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robots and their properties
num_robots = 8
capacity = 35
depot = 0

def calculate_distance_matrix(coordinates):
    """ Compute the Euclidean distance matrix between each pair of cities. """
    num_cities = len(coordinates)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = euclidean(coordinates[i], coordinates[j])
    return dist_matrix

def calculate_savings(dist_matrix):
    """ Calculate savings for each pair i, j as S_ij = d_0i + d_0j - d_ij. """
    num_cities = len(dist_matrix)
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            savings.append(((i, j), dist_matrix[depot][i] + dist_matrix[depot][j] - dist_matrix[i][j]))
    savings.sort(key=lambda x: x[1], reverse=True)
    return savings

def initial_solution(savings, demands):
    """ Create initial tours from savings list. """
    routes = []
    load = {i: 0 for i in range(num_robots)}
    routed = set([depot])
    available = set(range(1, len(demands)))
    
    for (i, j), _ in savings:
        if i in available and j in available:
            # Find a vehicle for new route if possible
            for k in range(num_robots):
                if load[k] + demands[i] + demands[j] <= capacity:
                    routes.append([depot, i, j, depot])
                    load[k] += demands[i] + demands[j]
                    available.remove(i)
                    available.remove(j)
                    break

    # Assign remaining cities as single trips
    for city in available:
        for k in range(num_robots):
            if load[k] + demands[city] <= capacity:
                routes.append([depot, city, depot])
                load[k] += demands[city]
                break

    return routes

def total_distance(route, dist_matrix):
    """ Calculate the total distance of a route. """
    return sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

def solution_cost(routes, dist_matrix):
    """ Calculate the total solution cost and costs per route. """
    costs = [total_distance(route, dist_matrix) for route in routes]
    total_cost = sum(costs)
    return costs, total_cost

# Run the algorithm
distance_matrix = calculate_distance_matrix(city_coordinates)
savings = calculate_savings(distance_matrix)
initial_routes = initial_solution(savings, demands)
route_costs, overall_cost = solution_cost(initial_routes, distance_matrix)

# Print routes and costs
for i, route in enumerate(initial_routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_costs[i]}")
print(f"Overall Total Travel Cost: {overall_cost}")