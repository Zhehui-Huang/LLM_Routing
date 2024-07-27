import math
import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and capacity
num_robots = 2
capacity = 160

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute cost matrix
def calculate_cost_matrix(coords):
    n = len(coords)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                cost_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return cost_matrix

cost_matrix = calculate_cost_matrix(coordinates)

# Clarke-Wright Savings Algorithm
def clarke_wright_savings(demands, cost_matrix, capacity):
    n = len(demands)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                sij = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings.append((sij, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    
    routes = [[0, i, 0] for i in range(1, n)]
    load = [demands[i] for i in range(n)]
    
    for s, i, j in savings:
        route_i = [r for r in routes if i in r][0]
        route_j = [r for r in routes if j in r][0]
        
        if route_i != route_j:
            if route_i[1] == i and route_j[-2] == j:
                new_route = route_j[:-1] + route_i[1:]
            elif route_j[1] == j and route_i[-2] == i:
                new_route = route_i[:-1] + route_j[1:]
            else:
                continue
            
            if sum(demands[k] for k in new_route if k != 0) <= capacity:
                routes.remove(route_i)
                routes.remove(route_j)
                routes.append(new_route)
    
    return routes

routes = clarke_wright_savings(demands, cost_matrix, capacity)

# Calculate route costs
def calculate_route_cost(route, cost_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += cost_matrix[route[i]][route[i + 1]]
    return cost

# Output solution
total_cost = 0
for robot_id, route in enumerate(routes[:num_robots]):
    route_cost = calculate_route_cost(route, cost_matrix)
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost}")
    total_cost += route_cost

print(f"Overall Total Travel Cost: {total_cost}")