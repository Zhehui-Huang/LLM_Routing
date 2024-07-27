import numpy as np
from math import sqrt

# City Coordinates and Demands
cities = {
    0: (30, 40),
    1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58),
    9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69)
}
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Parameters
num_cities = len(cities)
num_robots = 8
robot_capacity = 35

# Calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate cost matrix
cost_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Clarke-Wright Savings Algorithm Functions
def calculate_savings():
    savings = []
    for i in range(1, num_cities):
        for j in range(i+1, num_cities):
            s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def merge_routes(routes, capacity, demands, savings):
    route_map = {i: [i] for i in range(1, num_cities)}
    for _, i, j in savings:
        route_i = route_map[i]
        route_j = route_map[j]
        if route_i != route_j:
            if sum(demands[k] for k in route_i + route_j) <= capacity:
                for k in route_j:
                    route_map[k] = route_i
                route_i.extend(route_j)

    # Extract unique routes
    unique_routes = set(tuple(route_map[i]) for i in range(1, num_cities))
    return [list(route) for route in unique_routes]

def calculate_route_cost(route):
    cost = cost_matrix[0][route[0]] + cost_matrix[route[-1]][0]
    cost += sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    return cost

savings = calculate_savings()
routes = merge_routes(routes={}, capacity=robot_capacity, demands=demands, savings=savings)

# Display the output
overall_cost = 0
for idx, route in enumerate(routes):
    route_cost = calculate_route_cost(route)
    overall_cost += route_cost
    print(f"Robot {idx} Tour: [0, " + ', '.join(map(str, route)) + ", 0]")
    print(f"Robot {idx} Total Travel Cost: {route_cost}\n")

print(f"Overall Total Travel Cost: {overall_cost}")