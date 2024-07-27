import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random

# Provided city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40

# Compute the cost matrix
def calculate_cost_matrix(coords):
    n = len(coords)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cost_matrix[i][j] = euclidean(coords[i], coords[j])
    return cost_matrix

cost_matrix = calculate_cost_matrix(coordinates)

# Compute the savings matrix
def calculate_savings(cost_matrix):
    n = len(cost_matrix)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            saving = cost_matrix[i][0] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((saving, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

savings = calculate_savings(cost_matrix)

# Initial route construction using the Clarke-Wright Savings Algorithm
def initialize_routes(savings, demands, capacity):
    routes = []
    load = {i: 0 for i in range(num_robots)}
    in_route = {i: False for i in range(1, len(demands))}
    
    for saving, i, j in savings:
        # Find routes for i and j
        route_i, route_j = None, None
        for route in routes:
            if i in route:
                route_i = route
            if j in route:
                route_j = route
        
        if route_i is not None and route_j is not None and route_i != route_j:
            # merge condition checks capacity and if i and j are not in the same route
            if load[route_i] + load[route_j] <= capacity:
                combined_route = route_i + route_j
                routes.remove(route_i)
                routes.remove(route_j)
                routes.append(combined_route)
                load[combined_route] = load[route_i] + load[route_j]
        elif route_i is not None and not in_route[j]:
            if load[route_i] + demands[j] <= capacity:
                route_i.append(j)
                load[route_i] += demands[j]
                in_route[j] = True
        elif route_j is not None and not in_route[i]:
            if load[route_j] + demands[i] <= capacity:
                route_j.append(i)
                load[route_j] += demands[i]
                in_route[i] = True
        elif route_i is None and route_j is None:
            if demands[i] + demands[j] <= capacity:
                new_route = [i, j]
                routes.append(new_route)
                load[new_route] = demands[i] + demands[j]
                in_route[i] = in_route[j] = True
                
    # Check if there are cities not in any route
    for city in range(1, len(demands)):
        if not in_route[city]:
            if demands[city] <= capacity:
                routes.append([city])
                in_route[city] = True

    return routes

initial_routes = initialize_routes(savings, demands, robot_capacity)

# Convert route lists to start and end at the depot, compute the total cost
def finalize_routes(routes):
    final_routes = []
    total_cost = 0
    for route in routes:
        full_route = [0] + route + [0]
        route_cost = sum(cost_matrix[full_route[i]][full_route[i+1]] for i in range(len(full_route)-1))
        final_routes.append((full_route, route_cost))
        total_cost += route_cost
    return final_routes, total_cost

final_routes, total_cost = finalize_routes(initial_routes)

# Output result
for idx, (route, cost) in enumerate(final_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")