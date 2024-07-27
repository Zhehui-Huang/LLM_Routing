import numpy as np
import math
import random

# City coordinates and demand
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Number of robots and their capacity
num_robots = 8
capacity = 40

# Calculating the distance matrix
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Create initial solution
def initialize_solution():
    routes = [[] for _ in range(num_robots)]
    remaining_demands = demands[:]
    robot_capacity = [capacity] * num_robots
    unvisited = list(range(1, len(coordinates))) # Exclude the depot
    
    for vehicle in range(num_robots):
        if not unvisited:
            break
        current_city = 0
        routes[vehicle].append(current_city)
        load = 0
        
        while unvisited:
            next_city = min(unvisited, key=lambda x: distance_matrix[current_city][x] if robot_capacity[vehicle] >= remaining_demands[x] else float('inf'))
            if robot_capacity[vehicle] >= remaining_demands[next_city]:
                routes[vehicle].append(next_city)
                robot_capacity[vehicle] -= remaining_demands[next_city]
                load += remaining_demands[next_city]
                current_city = next_city
                unvisited.remove(next_city)
            else:
                break
        routes[vehicle].append(0)  # Return to depot

    return routes

# Calculate total distance of the route
def calculate_route_distance(route):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Improve solution using ALNS (sketch, to be implemented fully as needed)
def improve_solution(routes):
    # This function should be implemented with the actual ALNS algorithm
    # For now, we are returning the initial solution as is
    return routes

# Main execution
initial_routes = initialize_solution()
improved_routes = improve_solution(initial_routes)
total_cost = 0

for idx, route in enumerate(improved_routes):
    route_cost = calculate_route_distance(route)
    total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {round(route_cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")