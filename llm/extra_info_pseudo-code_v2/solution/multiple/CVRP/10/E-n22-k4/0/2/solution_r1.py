import numpy as np
from itertools import combinations

# Data: Coordinates and Demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot Information
num_robots = 4
robot_capacity = 6000

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cost matrix calculation
def create_cost_matrix(coords):
    n = len(coords)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return matrix

# Clarke-Wright Savings Algorithm Initialize
def compute_savings(cost_matrix):
    savings_list = []
    n = len(cost_matrix)
    for i in range(1, n):
        for j in range(i + 1, n):
            savings = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings_list.append((savings, i, j))
    savings_list.sort(reverse=True, key=lambda x: x[0])
    return savings_list

# Assigning routes considering capacity constraints
def assign_routes(savings_list, demands, capacity):
    routes = []
    load = {}
    route_demand = {}
    
    for s, i, j in savings_list:
        assigned = False
        for route in routes:
            if (i in route and j not in route) or (j in route and i not in route):
                if i in route:
                    idx, other = i, j
                else:
                    idx, other = j, i
                # Check capacity before adding
                if route_demand[route] + demands[other] <= capacity:
                    route.append(other)
                    route_demand[route] += demands[other]
                    assigned = True
                    break
        if not assigned:
            # Create new route if both are unassigned and their combined demands do not exceed capacity
            if demands[i] + demands[j] <= capacity:
                new_route = [0, i, j, 0]
                routes.append(new_route)
                route_demand[tuple(new_route)] = demands[i] + demands[j]

    return routes, route_demand
    
# Calculate routes and load
cost_matrix = create_cost_matrix(coordinates)
savings_list = compute_savings(cost_matrix)
routes, route_demand = assign_routes(savings_list, demands, robot_capacity)

# Output results
total_cost = 0
for index, route in enumerate(routes):
    tour_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_cost += tour_parul .cost
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")