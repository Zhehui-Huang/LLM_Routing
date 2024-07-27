import math
import numpy as np

# Coordinates and demands of the cities
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
robot_capacity = 6000

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate cost matrix
def generate_cost_matrix(coords):
    n = len(coords)
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return matrix

cost_matrix = generate_cost_matrix(coordinates)

# Clarke-Wright Savings Algorithm
def clarke_wright_savings(num_cities, demands, capacity, depot_idx=0):
    savings_list = []
    initial_routes = [[i] for i in range(1, num_cities)]  # excluding depot
    
    # Calculate savings
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                s_ij = cost_matrix[depot_idx][i] + cost_matrix[depot_idx][j] - cost_matrix[i][j]
                savings_list.append((s_ij, i, j))
    
    # Sort savings in descending order
    savings_list.sort(reverse=True, key=lambda x: x[0])
    
    routes = {i: [depot_idx, i, depot_idx] for i in range(1, num_cities)}
    load = {i: demands[i] for i in range(1, num_cities)}
    
    # Merge routes based on savings
    for _, i, j in savings_list:
        route_i = [r for r in routes if i in routes[r]][0]
        route_j = [r for r in routes if j in routes[r]][0]
        if route_i != route_b and (load[route_i] + load[route_j] <= capacity):
            # Check for connecting ends and capacity constraint
            if routes[route_i][-2] == i and routes[route_j][1] == j:
                # Merge routes
                new_route = routes[route_i][:-1] + routes[route_j][1:]
                load[route_i] += load[route_j]
                del routes[route_j], load[route_j]
                routes[route_i] = new_route

    return [routes[r] for r in routes]

# Generate initial solutions
routes = clarke_wright_savings(len(coordinates), demands, robot_capacity)

# Compute the cost for each route
def calculate_route_cost(route):
    cost = 0
    for i in range(len(route)-1):
        cost += cost_matrix[route[i]][route[i+1]]
    return cost

# Results
total_cost = 0
for idx, route in enumerate(routes):
    route_cost = calculate_route_cost(route)
    total_cost += route_cost
    print(f"Robot {idx % num_robots} Tour: {route}")
    print(f"Robot {idx % num_robots} Total Travel Cost: {route_cost}\n")

print(f"Overall Total Travel Cost: {total_cost}")