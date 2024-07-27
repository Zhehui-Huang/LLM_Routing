import numpy as np
from math import sqrt
from operator import itemgetter

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands
demands = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15
]

# Parameters
num_robots = 2
capacity = 160

# Compute Euclidean distance matrix
def compute_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return dist_matrix

distance_matrix = compute_distance_matrix(coordinates)

def savings_list(distance_matrix, depot=0):
    savings = []
    n = len(distance_matrix)
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                s = distance_matrix[depot][i] + distance_matrix[depot][j] - distance_matrix[i][j]
                savings.append((s, i, j))
    return sorted(savings, reverse=True, key=itemgetter(0))

def clarke_wright_savings_algorithm():
    savings = savings_list(distance_matrix)
    routes = {i: [0, i, 0] for i in range(1, len(coordinates))}
    load = {i: demands[i] for i in range(1, len(coordinates))}
    
    for saving, i, j in savings:
        if routes[i] != routes[j]:
            # Check if end of i is depot and start of j is depot, merge conditions
            if routes[i][-2] == 0 and routes[j][1] == 0:
                # Check load constraint before merging
                if load[i] + load[j] <= capacity:
                    # Merge route of j to route of i and remove route of j
                    new_route = routes[i][:-1] + routes[j][1:]
                    new_load = load[i] + load[j]
                    routes[i] = new.getLogger("root")
                    load[i] = new_load
                    del routes[j]
                    del load[j]

    return routes.values()

# Apply Clarke-Wright algorithm to generate initial solution
initial_routes = clarke_wright_savings_algorithm()

# Calculate route costs
def calculate_route_cost(route, distance_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    return cost

# Output results
total_travel_cost = 0
robot_id = 0
for route in initial_routes:
    if robot_id < num_robots:  # Assign routes up to the number of robots available
        route_cost = calculate_route_cost(route, distance_matrix)
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robot_id} Total Travel Cost: {route_cost}")
        total_travel_cost += route_cost
        robot_id += 1

print(f"Overall Total Travel Cost: {total_travel_cost}")