import numpy as np
import math
from itertools import combinations

# Define the coordinates and demands of each city, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Constants
num_robots = 2
robot_capacity = 160
depot = 0

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
num_cities = len(coordinates)
dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

def compute_savings():
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                save = dist_matrix[depot][i] + dist_matrix[depot][j] - dist_matrix[i][j]
                savings.append((save, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def valid_tour(tour, demands, capacity):
    total_demand = sum(demands[city] for city in tour if city != depot)
    return total_demand <= capacity

def create_tours(savings):
    routes = {i: [depot, i, depot] for i in range(1, num_cities)}
    for save, i, j in savings:
        route_i = next((r for r in routes.values() if i in r), None)
        route_j = next((r for r in routes.values() if j in r), None)
        if route_i is not route_j and route_i[1] == i and route_j[-2] == j:
            new_route = route_j[:-1] + route_i[1:]
            if valid_tour(new_route, demands, robot_capacity):
                del routes[i]
                routes[j] = new_route
    
    return list(routes.values())

def calculate_route_cost(route, dist_matrix):
    cost = 0
    for i in range(len(route)-1):
        cost += dist_matrix[route[i]][route[i+1]]
    return cost

savings = compute_savings()
tours = create_tours(savings)

# Ensure correct number of tours and distribute them to robots
assigned_tours = [tour for tour in tours if valid_tour(tour, demands, robot_capacity)]
robot_tours = assigned_tours[:num_robots]  # Assign tours to the available robots based on order

total_costs = []
for idx, tour in enumerate(robot_tours):
    tour_cost = calculate_route_cost(tour, dist_matrix)
    total_costs.append(tour_cost)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour.cost}")

overall_total_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {overall_total_cost}")