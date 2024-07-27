import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

def calculate_cost(route, dist_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += dist_matrix[route[i]][route[i + 1]]
    return cost

def two_opt(route, dist_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if calculate_cost(new_route, dist_matrix) < calculate_cost(best, dist_matrix):
                    best = new_route
                    improved = True
        route = best
    return best

# City coordinates (index 0 is the depot)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Distances among cities
dist_matrix = calculate_distance_matrix(cities)

# Number of robots
num_robots = 8

# Assign cities to robots (simple division, can be improved with more complex algorithms)
cities_per_robot = (len(cities) - 1) // num_robots

robots_routes = [[] for _ in range(num_robots)]

# Simple round-robin assignment
for i, city in enumerate(range(1, len(cities))):
    robots_routes[i % num_robots].append(city)

# Implement two-opt for each robot's route and calculate cost
overall_cost = 0

for idx, robot_route in enumerate(robots_routes):
    route_with_depot = [0] + robot_route + [0]
    optimized_route = two_opt(route_with_depot, dist_matrix)
    route_cost = calculate_cost(optimized_route, dist_matrix)
    print(f"Robot {idx} Tour: {optimized_route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")
    overall_cost += route_cost

print(f"Overall Total Travel Cost: {overall_cost}")