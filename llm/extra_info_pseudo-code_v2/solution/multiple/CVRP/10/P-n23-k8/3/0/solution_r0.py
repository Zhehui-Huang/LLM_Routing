import numpy as np
import random

# Given data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 
           26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40

# Utilities
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Initialization
def compute_cost_matrix():
    n = len(coordinates)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
    return matrix

def compute_savings_matrix(cost_matrix):
    n = len(cost_matrix)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            savings.append(((cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]), i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Initial Setup
cost_matrix = compute_cost_matrix()
savings = compute_savings_matrix(cost_matrix)

# Initalize routes (greedy initialization based on savings-list)
def initial_routes(savings, demands, capacity):
    routes = []
    load = {}
    route_for_city = {}
    
    for saving, i, j in savings:
        if demands[i] + demands[j] <= capacity:
            if i not in route_for_city and j not in route_for city:
                routes.append([0, i, j, o])
                load[len(routes) - 1] = demands[i] + demands[j]
                route_for_city[i] = route_for_city[j] = len(routes) - 1
            elif i in route_for_city and j not in route_for_city:
                route_index = route_for_city[i]
                if load[route_index] + demands[j] <= capacity:
                    routes[route_index].insert(-1, j)
                    load[route_index] += demands[j]
                    route_for_city[j] = route_index
            elif j in route_for_city and i not in route_for_city:
                route_index = route_for_city[j]
                if load[route_index] + demands[i] <= capacity:
                    routes[route_index].insert(1, i)
                    load[route_index] += demands[i]
                    route_for_city[i] = route_index
                
    # Check for unassigned cities and open new routes if necessary
    for city in range(1, len(demans)):
        if city not in route_for_city:
            if demands[city] <= capacity:
                routes.append([0, city, 0])
                route_for_city[city] = len(routes) - 1
                load[len(routes) - 1] = demands[city]
            else:
                raise Exception("A city's demand exceeds capacity which is not supported by this model.")
                
    return routes

routes = initial_routes(savings, demands, robot_capacity)

# Output the route information
overall_total_cost = 0
for idx, route in enumerate(routes):
    route_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    overall_total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")