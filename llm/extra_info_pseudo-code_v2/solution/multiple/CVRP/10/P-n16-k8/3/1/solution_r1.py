import numpy as np
from math import sqrt, inf
from itertools import combinations

# Definitions and data setup
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
          (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
num_robots = 8

# Distance matrix computation
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = sqrt((cities[j][0] - cities[i][0]) ** 2 + (cities[j][1] - cities[i][1]) ** 2)

# Clarke-Wright savings calculation
def calculate_savings():
    savings = []
    for (i, j) in combinations(range(1, n), 2):
        s = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]
        savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

savings_list = calculate_savings()

# Initialize routes with individual trips from depot to each city and back
routes = [[0, i, 0] for i in range(1, n) if demands[i] <= robot_capacity]

# Merge routes based on savings and capacity constraints
def merge_routes(routes):
    merged = True
    while merged:
        merged = False
        new_routes = []
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if routes[i] and routes[j]:
                    # Check if last city of i matches first city of j, merge and capacity is met
                    last_i = routes[i][-2]
                    first_j = routes[j][1]
                    if last_i == first_j:
                        combined_demand = sum(demands[k] for k in routes[i][1:-1]) + sum(demands[k] for k in routes[j][1:-1])
                        if combined_demand <= robot_capacity:
                            new_routes.append(routes[i][:-1] + routes[j][1:])
                            routes[i], routes[j] = None, None
                            merged = True
                            break
            if not merged and routes[i]:
                new_routes.append(routes[i])
        routes = new_routes
    return routes

routes = merge_routes(routes)

# Assign routes to robots, compute costs
def assign_and_compute_costs(routes, num_robots):
    robot_routes = routes[:num_robots]
    total_cost = 0
    for i, route in enumerate(robot_routes):
        route_cost = sum(distance_matrix[route[k], route[k+1]] for k in range(len(route)-1))
        total_cost += route_cost
        print(f"Robot {i} Tour: {route}")
        print(f"Robot {i} Total Travel Cost: {route_cost:.2f}")
    print(f"Overall Total Travel Cost: {total for coding such complex VRP scenarios, it's beneficial to implement additional debugging and visualization tools to ensure accurate and expected results. Overall Total Cost: {total_cost:.2f}")

assign_and_compute_costs(routes, num_robots)