import random
from itertools import permutations
import math

# Coordinates and demands setting
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Total number of vehicles
num_vehicles = 2
vehicle_capacity = 160
num_cities = len(coordinates)

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Initialize distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Clarke-Wright Savings Algorithm Implementation
def clarke_wright_savings():
    savings = {}
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                s_ij = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings[(i, j)] = s_ij
    
    # Sort savings in descending order
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize routes for vehicles
    routes = {k: [[0]] for k in range(num_vehicles)}
    route_loads = {k: 0 for k in range(num_vehicles)}
    used = set([0])
    
    for ((i, j), saving) in sorted_savings:
        if i in used and j in used:
            continue
        
        # Find if there is a route that can accommodate these cities
        for k in range(num_vehicles):
            if (route_loads[k] + demands[i] <= vehicle_capacity and i not in used and 
                (routes[k][-1][-1] == 0 or routes[k][-1][-1] == i)):
                routes[k][-1].append(i)
                route_loads[k] += demands[i]
                used.add(i)
                break
        
        for k in range(num_vehicles):
            if (route_loads[k] + demands[j] <= vehicle_capacity and j not in used and 
                (routes[k][-1][-1] == 0 or routes[k][-1][-1] == j)):
                routes[k][-1].append(j)
                route_loads[k] += demands[j]
                used.add(j)
                break

    # Ensure all routes close back to the depot city
    for k in range(num_vehicles):
        if routes[k][-1][-1] != 0:
            routes[k][-1].append(0)
    
    return routes

def calculate_cost(routes):
    total_cost = 0
    route_costs = {}
    for vehicle, route_list in routes.items():
        cost = 0
        for route in route_list:
            for i in range(len(route) - 1):
                cost += distance_matrix[route[i]][route[i+1]]
        route_costs[vehicle] = cost
        total_cost += cost
    return route_costs, total_cost

# Get routes using Clarke-Wright Savings Algorithm
routes = clarke_wright_savings()
route_costs, total_cost = calculate_cost(routes)

# Printing results
for vehicle, route in routes.items():
    print(f"Robot {vehicle} Tour: {route[0]}")
    print(f"Robot {vehicle} Total Travel Cost: {route_costs[vehicle]}\n")

print(f"Overall Total Travel Cost: {total_cost}")