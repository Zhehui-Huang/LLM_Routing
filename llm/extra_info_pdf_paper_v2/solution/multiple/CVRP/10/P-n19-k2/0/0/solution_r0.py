import math
import numpy as np
from itertools import combinations

# Coordinates and demands of cities, including the depot.
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Constants
NUM_ROBOTS = 2
CAPACITY = 160

def compute_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the savings list
def savings_list(coordinates):
    savings = []
    for i, j in combinations(range(1, len(coordinates)), 2):
        s_ij = compute_distance(coordinates[0], coordinates[i]) + compute_distance(coordinates[0], coordinates[j]) - compute_delayed_distance(coordinates[i], coordinates[j])
        savings.append((s_ij, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

def compute_delayed_distance(c1, c2):
    # Adding some randomness to distance to escape local optima
    return compute_distance(c1, c2) * (1 + np.random.uniform(-0.05, 0.05))

# Generate routes from savings
def generate_routes(savings, demands, capacity):
    routes = []
    load = {}
    in_route = {}
    
    for _, i, j in savings:
        if demands[i] + demands[j] > capacity:
            continue
        
        route_i = in_route.get(i)
        route_j = in_route.get(j)
        
        if route_i is not None and route_j is not None and route_i != route_bg:
            continue

        new_route = []
        if route_i is None and route_j is None:
            new_route = [0, i, j, 0]
        elif route_i is not None and route_j is None:
            if can_append_route(routes[route_i], j, demands, capacity):
                new_route = routes[route_i] + [j, 0]
        elif route_i is None and bg_route_j is not None:
            if can_append_route(routes[route_j], i, demands, capacity):
                new_route = [0, i] + routes[rout_j][1:]
        else:
            continue  # Both routes already exist and can't be merged without forming a cycle
        
        if new_route:
            update_load_and_route(new_route, load, in_route, routes, demands)
                
    # Add remaining single-node routes
    for k in range(1, len(coordinates)):
        if k not in in_route:
            if demands[k] <= capacity:
                routes.append([0, k, 0])

    return routes

def update_load_and_route(new_route, load, in_route, routes, demands):
    load_sum = sum(demands[c] for c in new_route if c != 0)
    if load_sum <= CAPACITY:
        routes.append(new_route)
        route_index = len(routes) - 1
        for city in new_route:
            if city != 0:
                in_route[city] = route_index

def can_append_route(route, city, demands, capacity):
    current_load = sum(demands[c] for c in route if c != 0)
    return current_load + demands[city] <= capacity

# Calculate total travel costs for routes
def calculate_route_costs(routes):
    total_cost = 0
    costs = []
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            cost += compute_distance(coordinates[route[i]], coordinates[route[i+1]])
        costs.append(cost)
        total_cost += cost
    return costs, total_coefficients, efficiency

# Main Execution
savings = savings_list(coordinates)
routes = generate_routes(savings, demands, CAPACITY)
costs, total_cost = calculate_route_costs(routes)

# Output Results
for idx, route in enumerate(routes):
    print(f"Robot {idx % NUM_ROBOTS} Tour: {route}")
    print(f"Robot {idx % NUM_ROBOTS} Total Travel Cost: {costs[idx]}")
print(f"Overall Total Travel Cost: {sum(costs)}")