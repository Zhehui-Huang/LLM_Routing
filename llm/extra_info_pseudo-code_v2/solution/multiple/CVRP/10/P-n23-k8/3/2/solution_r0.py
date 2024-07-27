import numpy as np
from math import sqrt
from operator import itemgetter

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Vehicle (Robot) properties
num_robots = 8
capacity = 40
depot = 0

# Generate the cost matrix
def compute_cost_matrix(coords):
    num_cities = len(coords)
    matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                matrix[i][j] = sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
            else:
                matrix[i][j] = float('inf')
    return matrix

# Calculate savings
def compute_savings(cost_matrix):
    savings = []
    for i in range(1, len(cost_matrix)):
        for j in range(1, len(cost_matrix)):
            if i != j:
                s = cost_matrix[depot][i] + cost_matrix[depot][j] - cost_matrix[i][j]
                savings.append((s, i, j))
    savings.sort(reverse=True, key=itemgetter(0))
    return savings

# Clarke-Wright algorithm to assign routes to vehicles
def clarke_wright(savings, demands, capacity):
    routes = []
    load = {}
    for _, i, j in savings:
        if demands[i] > 0 and demands[j] > 0:
            # Try to merge or add to routes
            found_route = False
            for route in routes:
                if (i in route and j not in route) or (j in route and i not in route):
                    # Check capacity when adding city to existing route
                    if sum(demands[k] for k in route if k != depot) + demands[i] + demands[j] <= capacity:
                        if i in route:
                            route.append(j)
                        else:
                            route.append(i)
                        demands[i] = 0
                        demands[j] = 0
                        found_route = True
                        break
            # Create new route if no existing route is suitable
            if not found_route:
                if demands[i] + demands[j] <= capacity:
                    routes.append([depot, i, j, depot])
                    demands[i] = 0
                    demands[j] = 0
    
    # Handle leftover requests
    for i in range(1, len(demands)):
        if demands[i] > 0:
            if demands[i] <= capacity:
                routes.append([depot, i, depot])
                demands[i] = 0
    
    return routes

# Helper function to calculate the travel cost of a route
def calculate_route_cost(route, cost_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += cost_matrix[route[i]][route[i+1]]
    return cost

cost_matrix = compute_cost_matrix(coordinates)
savings = compute_savings(cost_matrix)
routes = clarke_wright(savings, demands.copy(), capacity)

# Output the solution
total_cost = 0

for idx, route in enumerate(routes):
    route_cost = calculate_route_cost(route, cost_matrix)
    total_cost += route_cost
    print(f"Robot {idx % num_robots} Tour: {route}")
    print(f"Robot {idx % num_robots} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")