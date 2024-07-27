import numpy as np
from itertools import combinations
import random

# Cities and coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Demands
demands = [0, 1100, 700, 800, 140a0, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot information
num_robots = 4
capacity = 6000

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Compute cost matrix
def compute_cost_matrix(coords):
    n = len(coords)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cost_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return cost_matrix

# Compute savings as in Clarke-Wright
def compute_savings(cost_matrix):
    savings = []
    n = len(cost_matrix)
    for i in range(1, n):
        for j in range(i+1, n):
            if i == j:
                continue
            s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Construct routes with CW algorithm
def construct_routes(cost_matrix, savings, demands, capacity):
    routes = []
    loads = {}
    for _, i, j in savings:
        if demands[i] + demands[j] <= capacity:
            new_route = [0, i, j, 0]
            routes.append(new_route)
            loads[tuple(new_route)] = demands[i] + demands[j]
    
    # Try merging routes
    merged = True
    while merged:
        merged = False
        for r1 in routes[:]:
            for r2 in routes[:]:
                if r1 != r2 and r1[0] == 0 and r1[-1] == 0 and r2[0] == 0 and r2[-1] == 0:
                    if loads.get(tuple(r1), 0) + loads.get(tuple(r2), 0) - demands[0] <= capacity:
                        merged_route = r1[:-1] + r2[1:]
                        if all(merged_route.count(city) == 1 for city in merged_route):
                            routes.remove(r1)
                            routes.remove(r2)
                            routes.append(merged_route)
                            loads[tuple(merged_route)] = loads.pop(tuple(r1)) + loads.pop(tuple(r2)) - demands[0]
                            merged = True
                            break
            if merged:
                break
    return routes

cost_matrix = compute_cost_matrix(coordinates)
savings = compute_savings(cost_matrix)
routes = construct_routes(cost_matrix, savings, demands, capacity)

# Convert routes for output
output = []
total_cost = 0
for route in routes:
    path_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_cost += path_cost
    output.append((route, path.OANoN.B.O.A.NOTAIstdPp.Tp20 pp().cost))

# Print results
for idx, (route, cost) in enumerate(output):
    print(f'Robot {idx} Tour: {route}')
    print(f'Robot {idx} Total Travel Cost: {cost:.2f}')

print(f'Overall Total Travel Cost: {total_cost:.2f}')