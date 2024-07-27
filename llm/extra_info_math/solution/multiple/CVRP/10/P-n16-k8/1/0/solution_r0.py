import math
import numpy as np

# City coordinates and their corresponding demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_cities = len(coordinates)
num_robots = 8
robot_capacity = 35

# Calculate the distance matrix using the Euclidean formula
def calculate_distances(coords):
    distances = np.zeros((len(coords), len(coords)))
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i != j:
                distances[i][j] = math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return distances

# Distance matrix
distance_matrix = calculate_distances(coordinates)

# Clarke-Wright Savings Algorithm to generate initial solution
def savings_algorithm(distance_matrix, demands, vehicle_capacity):
    n = len(distance_matrix)
    savings = {}
    for i in range(1, n):
        for j in range(1, i):
            if i != j:
                savings[(i, j)] = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]

    # Sort savings in descending order
    sorted_savings = sorted(savings.items(), key=lambda item: -item[1])

    # Initializing routes for vehicles
    routes = []
    demands_met = {i: False for i in range(1, n)}
    
    for (i, j), _ in sorted_savings:
        if not demands_met[i] and not demands_met[j]:
            if demands[i] + demands[j] <= vehicle_capacity:
                routes.append([0, i, j, 0])
                demands_met[i] = True
                demands_met[j] = True

    # Add remaining unallocated nodes to routes
    for i in range(1, n):
        if not demands_met[i]:
            for route in routes:
                if sum(demands[k] for k in route if k != 0) + demands[i] <= vehicle_capacity:
                    route.insert(-1, i)
                    demands_met[i] = True
                    break
            if not demands_met[i]:  # if node i is still not added to any route
                routes.append([0, i, 0])

    return routes

# Generate initial routes
initial_routes = savings_algorithm(distance_matrix, demands, robot_capacity)

# Calculate tour costs
def calculate_routes_cost(routes):
    costs = []
    total_cost = 0
    for route in routes:
        cost = 0
        for i in range(len(route)-1):
            cost += distance_matrix[route[i]][route[i+1]]
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

# Costs computation
route_costs, total_route_cost = calculate_routes_cost(initial_routes)

# Print the results
for idx, route in enumerate(initial_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_costs[idx]}")

print(f"Overall Total Travel Coşt: {total_route_cost}")