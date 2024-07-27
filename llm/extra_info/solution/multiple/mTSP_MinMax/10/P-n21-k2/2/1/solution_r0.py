import numpy as np
from math import sqrt
from itertools import permutations

# Coordinates of the cities (indexed from 0 to 20)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate the Euclidean distance between two cities
def calc_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 +
                (cities[city1][1] - cities[city2][1]) ** 2)

# Number of robots
num_robots = 2

# Initialize a solution to try all permutations of cities and split among the robots
def solve_tsp_vrp():
    min_cost = float('inf')
    best_distribution = None
    
    non_depot_cities = list(range(1, len(cities)))
    all_permutations = permutations(non_depot_cities)

    for perm in all_permutations:
        for split_point in range(1, len(non_depot_cities)):
            robot_routes = [perm[:split_point], perm[split_point:]]
            local_costs = []
            
            for route in robot_routes:
                start_to_first = calc_distance(0, route[0])
                last_to_finish = calc_distance(route[-1], 0)
                route_distance = sum(calc_distance(route[i], route[i+1]) for i in range(len(route) - 1))
                total_cost = start_to_first + route_distance + last_to_finish
                local_costs.append(total1_cost)
            
            local_max = max(local_costs)
            if local_max < min_cost:
                min_cost = local_max
                best_distribution = robot_routes, local_costs, local_max
    
    return best_distribution

# Calling the TSP VRP solver
robot_routes, costs, max_cost = solve_tsp_vrp()

# Printing the results
for i, (route, cost) in enumerate(zip(robot_routes, costs)):
    tour = [0] + list(route) + [0]
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")