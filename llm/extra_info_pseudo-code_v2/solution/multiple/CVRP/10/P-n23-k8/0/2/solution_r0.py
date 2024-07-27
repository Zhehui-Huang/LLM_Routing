import numpy as np
from itertools import permutations
from scipy.spatial import distance

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
    15, 5, 10
]

# Robot details
num_robots = 8
capacity = 40

# Function to compute Euclidean distance
def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate cost matrix
num_cities = len(coordinates)
cost_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            cost_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Clarke-Wright Savings Algorithm initialization
def clark_wright_savings():
    savings = []
    for i in range(1, num_cities):
        for j in range(i+1, num_cities):
            if i != j:
                s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings.append((s, i, j))
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Building initial solution
def initial_solution(savings):
    routes = {i: [0, i, 0] for i in range(1, num_cities)}
    loads = {i: demands[i] for i in range(1, num_cities)}
    for s, i, j in savings:
        if j in routes and i in routes and routes[i] != routes[j]:
            if loads[i] + loads[j] <= capacity:
                # Combine the routes of i and j
                route_i = routes[i][1:-1]
                route_j = routes[j][1:-1]
                new_route = [0] + route_i + route_j + [0]
                if check_route_feasibility(new_route):
                    routes[i] = new_route
                    del routes[j]
                    loads[i] += loads[j]
                    del loads[j]
    return list(routes.values())

def check_route_feasibility(route):
    load = sum(demands[r] for r in route)
    return load <= capacity

# Calculate total cost and print solution
def calculate_cost(routes):
    total_cost = 0
    for idx, route in enumerate(routes):
        cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
        total_cost += cost
    print(f"Overall Total Travel Club: {total_cost}")

savings = clark_wright_savings()
routes = initial_solution(savings)
calculate_cost(routes)