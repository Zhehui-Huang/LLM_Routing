import numpy as arg
from scipy.spatial.distance import euclidean
from itertools import permutations

# Given City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_robots = 8
depot = 0

def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Partitioning cities (excluding depot) among robots
city_indices = list(cities.keys())[1:]  # [1, 2, ..., 15]
chunks = [city_indices[i::num_robots] for i in range(num_robots)]

# Function to calculate route cost
def calculate_route_cost(route):
    return sum(calculate_distance(route[i], route[i+1]) for i in range(len(route)-1))

# Function to find best path for given cities
def find_best_path(cities):
    min_route = None
    min_cost = float('inf')
    for route in permutations(cities):
        route = [depot] + list(route) + [depot]
        cost = calculate_route_cost(route)
        if cost < min_cost:
            min_cost = cost
            min_route = route
    return min_route, min_cost

# Assign routes and costs to robots and compute the total cost
total_cost = 0
for robot_id in range(num_robots):
    # Find best path and cost for the cities assigned to this robot
    assigned_cities = chunks[robot_id]
    best_route, best_cost = find_best_sequence(assigned_cities)
    total_cost += best_cost
    
    print(f"Robot {robot_id} Tour: {best_route}")
    print(f"Robot {robot_id} Total Travel Cost: {best_cost}")

print(f"Overall Total Travel Cost: {total_cost}")