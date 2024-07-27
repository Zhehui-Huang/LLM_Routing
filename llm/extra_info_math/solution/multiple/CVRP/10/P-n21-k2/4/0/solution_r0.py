import math
import numpy as np
from collections import deque

# Coordinates and demand list
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Costs as Euclidean distances between cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
n = len(coordinates)  # number of cities
dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Parameters
num_robots = 2
capacity = 160

# A simple heuristic to create initial feasible routes: Nearest Neighbor with capacity constraint
def nearest_neighbor_cvrp():
    unvisited = set(range(1, n))
    routes = []
    demands_fulfilled = [0] * num_robots
    
    for r in range(num_robots):
        current_city = 0
        tour = [current_city]
        load = 0

        while unvisited and load < capacity:
            next_city = min(unvisited, key=lambda x: dist_matrix[current_city][x] if demands[x] + load <= capacity else float('inf'))
            if demands[next_city] + load <= capacity:
                tour.append(next_city)
                load += demands[next_city]
                current_city = next_city
                unvisited.remove(next_city)
            else:
                break
        
        tour.append(0)  # return to depot
        routes.append(tour)
        demands_fulfilled[r] = load
    
    return routes, demands_fulfilled

# Calculate the total travel cost of tours
def calculate_cost(routes):
    total_cost = 0
    costs = []
    for tour in routes:
        cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

# Generate initial solution and compute its cost
initial_routes, _ = nearest_neighbor_cvrp()
costs, total_cost = calculate_cost(initial_routes)

# Print tours and costs
for idx, route in enumerate(initial_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")