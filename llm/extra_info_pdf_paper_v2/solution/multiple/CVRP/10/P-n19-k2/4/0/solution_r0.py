import random
import numpy as np
from math import sqrt

# Parameters
cities_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
num_robots = 2
robot_capacity = 160
num_cities = len(cities_coordinates)

def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_savings():
    savings = []
    d0 = [euclidean_distance(0, i) for i in range(num_cities)]
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s = d0[i] + d0[j] - euclidean_distance(i, j)
            savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

def initialize_routes():
    # Initial routes: each city is a separate route
    return [[i] for i in range(num_cities)]

def merge_routes(routes, savings):
    route_map = {i: i for i in range(num_cities)}
    capacity_map = {i: demands[i] for i in range(num_cities)}

    for _, i, j in savings:
        ri = route_map[i]
        rj = route_map[j]
        if ri != rj and ri != 0 and rj != 0:
            # Check if merging is possible within capacity constraints
            if capacity_map[ri] + capacity_map[rj] <= robot_capacity:
                # Merge routes
                new_route = routes[ri] + routes[rj]
                new_capacity = capacity_map[ri] + capacity_map[rj]
                # Update all indices in new route
                for city in routes[rj]:
                    route_map[city] = ri
                routes[ri] = new_route
                capacity_map[ri] = new_capacity
                # Empty the merged route
                routes[rj] = []
                capacity_map[rj] = 0
    # filter out empty routes and ignore routes only containing depot
    return [r for r in routes if r != [] and len(r) > 1]

def calculate_route_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += euclidean_distance(route[i - 1], route[i])
    # return to depot
    cost += euclidean_distance(route[-1], 0)
    return cost

def assign_and_optimize_routes(routes):
    random.shuffle(routes)  # Simulate the probabilistic assignment to robots
    # Split routes roughly evenly to robots, with consideration of total demands
    robot_routes = [[] for _ in range(num_robots)]
    robot_loads = [0] * num_robots
    robot_costs = [0] * num_robots

    for route in routes:
        # Assign route to least loaded robot
        min_robot = min(range(num_robots), key=lambda k: robot_loads[k])
        robot_routes[min_robot].append(route)
        route_demand = sum(demands[city] for city in route)
        robot_loads[min_robot] += route_demand
        route_cost = calculate_route_cost([0] + route + [0])
        robot_costs[min_robot] += route_cost

    return robot_routes, robot_costs

# Main execution flow
savings_list = calculate_savings()
routes = initialize_routes()
merged_routes = merge_routes(routes, savings_list)
assigned_routes, route_costs = assign_and_optimize_routes(merged_routes)

# Output results
total_cost = sum(route_costs)
for i in range(num_robots):
    full_route = [0] + [city for route in assigned_routes[i] for city in route] + [0]
    print(f"Robot {i} Tour: {full_route}")
    print(f"Robot {i} Total Travel Cost: {route_cost[i]}")
print("Overall Total Travel Cost:", total_cost)