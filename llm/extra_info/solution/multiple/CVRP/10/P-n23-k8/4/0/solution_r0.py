import math
import numpy as np

# City coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
vehicle_capacity = 40

# Helper functions
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_distance(tour, coords):
    total_dist = 0
    for i in range(1, len(tour)):
        total_dist += euclidean_distance(coords[tour[i - 1]], coords[tour[i]])
    return total_dist

# Construction heuristic: Clarke and Wright Savings Algorithm
def savings_algorithm(coords, demands, vehicle_capacity):
    num_cities = len(coords)
    savings_list = []
    routes = [[i] for i in range(1, num_cities)]

    # Compute savings
    for i in range(1, num_cities):
        for j in range(i+1, num_cities):
            if i != j:
                s = euclidean_distance(coords[0], coords[i]) + euclidean_distance(coords[0], coords[j]) - euclidean_distance(coords[i], coords[j])
                savings_list.append((s, i, j))
    savings_list.sort(reverse=True, key=lambda x: x[0])

    # Clustering
    for s, i, j in savings_list:
        # Find route containing i
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        if route_i != route_j and route_i is not None and route_j is not None:
            if route_i[0] == i and route_j[-1] == j:
                # Check capacity constraint before merging
                if sum(dem
ands[r] for r in route_i) + sum(demands[r] for r in route_j) <= vehicle_capacity:
                    route_j.extend(route_i)
                    routes.remove(route_i)

    # Add depot back to the routes
    final_routes = [[0] + route + [0] for route in routes if len(route) > 0]
    return final_routes

# Generate initial routes
initial_routes = savings_algorithm(coordinates, demands, vehicle_capacity)

# Improve routes with a 2-opt local search
def two_opt(route, coords):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if calculate_total_distance(new_route, coords) < calculate_total_distance(best, coords):
                    best = new_route
                    improved = True
    return best

optimized_routes = [two_opt(route, coordinates) for route in initial_routes]

# Calculate costs
total_costs = [calculate_total_distance(route, coordinates) for route in optimized_routes]
overall_cost = sum(total_csosts)

for idx, route in enumerate(optimized_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {total_costs[idx]}")

print(f"Overall Total Travel Cost: {overall_cost}")