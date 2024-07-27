import numpy as np
import itertools
from scipy.spatial.distance import euclidean

# City coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
               (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Parameters
num_robots = 8
robot_capacity = 40
depot = 0

# Helper function to calculate the Euclidean distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            dist = euclidean(coords[i], coords[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

# Compute cost matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Clarke-Wright Savings Algorithm
def cw_savings(dist_matrix, depot, demands, vehicle_capacity):
    num_cities = len(dist_matrix)
    savings = [(i, j, dist_matrix[depot][i] + dist_matrix[depot][j] - dist_matrix[i][j]) 
               for i in range(1, num_cities) for j in range(i+1, num_cities)]
    savings.sort(key=lambda x: x[2], reverse=True)
    
    routes = {}
    route_load = {}
    route_idx = 0

    in_route = {}
    for i in range(1, num_cities):
        routes[route_idx] = [depot, i, depot]
        route_load[route_idx] = demands[i]
        in_route[i] = route_idx
        route_idx += 1
    
    for s in savings:
        i, j, saving = s
        if i in in_route and j in in_route:
            ri, rj = in_route[i], in_route[j]
            if ri != rj and route_load[ri] + route_load[rj] <= vehicle_capacity:
                routes[ri] = [depot] + routes[ri][1:-1] + routes[rj][1:-1] + [depot]
                route_load[ri] += route_load[rj]
                del routes[rj], route_load[rj]
                for city in routes[ri][1:-1]:
                    in_route[city] = ri
    
    return routes

# Solve the CVRP
routes = cw_savings(distance_matrix, depot, demands, robot_capacity)

# Calculate total cost and display the solution
overall_cost = 0
for idx, route in routes.items():
    cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    overall_cost += cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")