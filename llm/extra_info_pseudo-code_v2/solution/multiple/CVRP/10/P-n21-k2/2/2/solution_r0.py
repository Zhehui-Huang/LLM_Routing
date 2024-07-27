import numpy as np
import math

# Provided city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 
    19, 11, 12, 26, 17, 6, 15
]

num_cities = len(coordinates)
num_robots = 2
robot_capacity = [160, 160]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a cost matrix based on Euclidean distance.
def calculate_cost_matrix(coords):
    n = len(coords)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                cost_matrix[i][j] = euclidean_distance(coords[i], coords[j])
            else:
                cost_matrix[i][j] = 0
    return cost_matrix

# Calculate initial savings as defined by the Clarke-Wright formula: Sij = C0i + C0j - Cij
def calculate_savings_matrix(cost_matrix):
    n = len(cost_matrix)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            saving = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((saving, i, j))
    # Sort savings by descending order
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

cost_matrix = calculate_cost_matrix(coordinates)
savings_list = calculate_savings_matrix(cost_matrix)

# A basic form of CVRP solver using a simplified Clarke-Wright algorithm.
def clarke_wright_solver(cost_matrix, savings_list, demands, num_vehicles, vehicle_capacity):
    routes = {k: [(0)] for k in range(num_vehicles)}  # All vehicles start at the depot
    remaining_capacity = {k: vehicle_capacity[k] for k in range(num_vehicles)}
    used = [False] * num_cities
    
    for saving, i, j in savings_list:
        if used[i] or used[j]:
            continue
        # Assignment of the route to the first available vehicle if both can be added.
        for k in range(num_vehicles):
            if remaining_capacity[k] >= demands[i] + demands[j] and routes[k][-1] == 0:
                routes[k].extend([i, j, 0])
                used[i] = True
                used[j] = True
                remaining_capacity[k] -= (demands[i] + demands[j])
                break
            
    # Assigning left over cities to any available route
    for i in range(1, num_cities):
        if not used[i]:
            for k in range(num_vehicles):
                if remaining_capacity[k] >= demands[i] and routes[k][-1] == 0:
                    routes[k].insert(-1, i)
                    used[i] = True
                    remaining_capacity[k] -= demands[i]
                    break

    return routes

routes = clarke_wright_solver(cost_matrix, savings_list, demands, num_robots, robot_capacity)

# Calculate cost for the routes
def calculate_route_cost(route, cost_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += cost_matrix[route[i]][route[i + 1]]
    return cost

total_cost = 0
for r in routes:
    route = routes[r]
    route_cost = calculate_route_cost(route, cost_matrix)
    total_cost += route_cost
    print(f"Robot {r} Tour: {route}")
    print(f"Robot {r} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")