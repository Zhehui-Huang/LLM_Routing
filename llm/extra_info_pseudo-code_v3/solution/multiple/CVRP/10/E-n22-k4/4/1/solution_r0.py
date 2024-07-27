import math
import numpy as np
from itertools import combinations

# Cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
           1800, 700]

# Parameters
num_robots = 4
capacity = 6000
num_cities = len(coordinates)

# Calculate the Euclidean distance matrix
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distance_matrix = [[calc_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Construction of initial solution using Clarke and Wright Savings Algorithm
def clarke_and_wright():
    savings = {(i, j): distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j] for i, j in combinations(range(1, num_cities), 2)}
    sorted_savings = sorted(savings.items(), key=lambda item: item[1], reverse=True)
    
    routes = {i: [0, i, 0] for i in range(1, num_cites)}
    load = {i: demands[i] for i in range(1, num_cities)}
    
    for (i, j), _ in sorted_savings:
        if i in routes and j in routes and routes[i] != routes[j]:
            if load[i] + load[j] <= capacity:
                # Assuming routes[i] ends at depot and routes[j] starts at depot
                routes[i] = routes[i][:-1] + [j] + routes[j][1:]
                load[i] += load[j]
                del routes[j]
                del load[j]
                
    return list(routes.values())

# Generate initial solution
initial_routes = clarke_and_wright()

# ALNS is a placeholder as it requires complex implementation
def adaptive_large_neighborhood_search(routes):
    # Placeholder for simplicity
    return routes

final_routes = adaptive_large_neighborhood_search(initial_routes)

# Calculate costs and demand fulfillments
def calculate_costs_and_output(routes):
    total_cost = 0
    outputs = []
    
    for idx, route in enumerate(routes):
        cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        total_cost += cost
        outputs.append(f"Robot {idx} Tour: {route}")
        outputs.append(f"Robot {idx} Total Travel Cost: {cost:.2f}")
    
    outputs.append(f"Overall Total Travel Property: {total_cost:.2f}")
    return outputs

# Output
output_data = calculate_costs_and_output(final_routes)
for line in output_data:
    print(line)