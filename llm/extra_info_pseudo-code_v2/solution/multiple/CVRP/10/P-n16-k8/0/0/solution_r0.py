import math
from itertools import combinations
import random

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Demand list
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot parameters
num_robots = 8
robot_capacity = 35

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_cost_matrix():
    n = len(coordinates)
    cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]
    return cost_matrix

def calculate_savings(cost_matrix):
    savings = []
    depot = 0
    n = len(cost_matrix)
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                saving = cost_matrix[depot][i] + cost_matrix[depot][j] - cost_matrix[i][j]
                savings.append((saving, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def build_initial_routes(savings, demands, capacity):
    routes = []
    load = {}
    for _, i, j in savings:
        if demands[i] + demands[j] <= capacity:
            routes.append([0, i, j, 0])
            load[(i, j)] = demands[i] + demands[j]
            demands[i] = 0  # Mark as served
            demands[j] = 0  # Mark as served
    return routes, load

def calculate_route_cost(route, cost_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += cost_matrix[route[i]][route[i+1]]
    return cost

def main():
    cost_matrix = calculate_cost_matrix()
    savings = calculate_savings(cost_matrix)
    routes, load = build_initial_routes(savings, demands, robot_capacity)

    # Initialize total travel cost
    total_travel_cost = 0
    for route_id, route in enumerate(routes):
        route_cost = calculate_route_cost(route, cost_matrix)
        print(f"Robot {route_id} Tour: {route}")
        print(f"Robot {route_id} Total Travel Cost: {route_cost}")
        total_travel_cost += route_cost

    print(f"Overall Total Travel Cost: {total_travel_cost}")

main()