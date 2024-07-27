import numpy as np
from scipy.spatial.distance import euclidean
from random import sample, seed
from copy import deepcopy

# Set the seed for reproducibility
seed(0)

# Coordinates of Cities including Depot
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

n_cities = len(coordinates)
n_robots = 8

# Calculate Distance Matrix
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

# Initial greedy distribution of cities to robots
def initial_solution():
    cities = list(range(1, n_cities))
    robots = {k: [] for k in range(n_robots)}
    city_idx = 0
    
    while cities:
        robots[city_idx % n_robots].append(cities.pop(0))
        city_idx += 1
        
    for r in robots:
        robots[r] = [0] + robots[r] + [0]  # start and end at the depot
    
    return robots

# Calculate tour cost for each robot
def calculate_tour_costs(robots, distance_matrix):
    tour_costs = {}
    max_cost = 0
    for key in robots:
        tour = robots[key]
        cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        tour_costs[key] = cost
        if cost > max_cost:
            max_cost = cost
    return tour_costs, max_cost

# Simple 2-opt local search to optimize individual routes
def two_opt(route, distance_matrix):
    best = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # changes nothing, skip
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if sum(distance_matrix[new_route[k]][new_route[k+1]] for k in range(len(new_route) - 1)) < \
                        sum(distance_matrix[best[k]][best[k+1]] for k in range(len(best) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Generate the initial solution
robots = initial_solution()

# Apply local search (2-opt) to each robot's tour to possibly improve them
optimized_robots = {}
for r in robots:
    optimized_robots[r] = two_opt(robots[r], distance_matrix)

# Calculate and output the results
costs, max_cost = calculate_tour_costs(optimized_robots, distance_matrix)
for r in costs:
    print(f"Robot {r} Tour: {optimized_robots[r]}")
    print(f"Robot {r} Total Travel Cost: {costs[r]}")

print(f"Maximum Travel Cost: {max_cost}")