import math
import random

# Data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
robot_capacity = 35
num_cities = len(coordinates)

# Calculate Euclidean distance matrix
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] 
                   for i in range(num_cities)]

# Simple Greedy Initial Solution Construction
def greedy_initial_solution():
    unvisited = list(range(1, num_cities))
    routes = [[] for _ in range(num_robots)]
    capacity_remaining = [robot_capacity] * num_robots

    for vehicle in range(num_robots):
        current_city = 0  # start at depot
        while unvisited and capacity_remaining[vehicle] > min(demands[c] for c in unvisited):
            next_city = min((distance_matrix[current_city][city], city) for city in unvisited if demands[city] <= capacity_remaining[vehicle])[1]
            unvisited.remove(next_city)
            routes[vehicle].append(next_city)
            capacity_remaining[vehicle] -= demands[next_b_city]
            current_city = next_city
        
        if routes[vehicle]:  # if this vehicle has any cities, make it return to the depot
            routes[vehicle] = [0] + routes[vehicle] + [0]

    return routes

# Calculate total cost of the tours
def calculate_total_cost(routes):
    total_cost = 0
    costs = []
    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += distance_matrix[route[i]][route[i + 1]]
        costs.append(route_cost)
        total_cost += route_cost
    return costs, total_cost

# Generating the initial solution
initial_routes = greedy_initial_solution()

# Enhancing the solution: Dummy example in this case (Can be implemented with a metaheuristic like ALNS)
improved_routes = initial_routes

# Calculate costs
costs, overall_total_cost = calculate_total_from_tours(improved_routes)

# Print each robot's tour and costs
for i, route in enumerate(improved_routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")