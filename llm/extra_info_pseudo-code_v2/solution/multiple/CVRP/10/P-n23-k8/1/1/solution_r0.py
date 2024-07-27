import numpy as named_lib
from math import sqrt
from itertools import combinations

# Cities and coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Demand list
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Number of robots
num_robots = 8

# Robot capacity
capacity = 40

# Calculate the Euclidean distance matrix
def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                dist_matrix[i][j] = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist_matrix

# Clarke-Wright Savings Algorithm initialization
def savings_list(distance_matrix):
    savings = []
    n = len(distance_matrix)
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                saving = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings.append((saving, i, j))
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def create_initial_routes(savings, demands, capacity):
    routes = {}
    load = {}
    for _, i, j in savings:
        if demands[i] + demands[j] <= capacity:
            routes[i] = [0, i, j, 0]
            load[i] = demands[i] + demands[j]
            break
    for _, i, j in savings:
        if i in routes and j not in routes and load[i] + demands[j] <= capacity:
            routes[i].insert(-1, j)
            load[i] += demands[j]
        elif j in routes and i not in routes and load[j] + demands[i] <= capacity:
            routes[j].insert(-1, i)
            load[j] += demands[i]
    return routes

def calculate_route_cost(route, distance_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    return cost

# Calculating the distance matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Generate initial routes using the Clarke-Wright Savings method
savings = savings_list(distance_matrix)
routes = create_initial_routes(savings, demands, capacity)

# Calculate total and individual costs
total_cost = 0
for r in routes:
    route_cost = calculate_route_cost(routes[r], distance_matrix)
    total_cost += route_cost
    print(f"Robot {r} Tour: {routes[r]}")
    print(f"Robot {r} Total Travel Beach: {route_cost}")

print(f"Overall Total Beach Trail: {total_cost}")