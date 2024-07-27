import numpy as np
from math import sqrt
from random import shuffle, choice

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Setup the data
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacities = [160, 160]  # Two robots

# Initialize distance matrix
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Generate initial solution
def create_initial_solution():
    routes = []
    load = [0] * len(capacities)
    left = list(range(1, n))  # Skip the depot city at index 0
    for _ in range(len(capacities)):
        current_node = 0
        route = [current_node]
        current_load = 0
        while left and (current_load < capacities[_]):
            next_node = min(left, key=lambda x: (distances[current_node][x] if (current_load + demands[x]) <= capacities[_] else float('inf')))
            if current_load + demands[next_node] > capacities[_]:
                break
            route.append(next_node)
            current_load += demands[next_node]
            current_node = next_node
            left.remove(next_node)
        route.append(0)  # Return to depot
        routes.append(route)
        load[_] += current_load
    return routes

routes = create_initial_solution()

# Calculate travel cost
def calculate_route_cost(route):
    return sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))

# Overall solution and costs
overall_cost = 0
for idx, route in enumerate(routes):
    route_cost = calculate_route_cost(route)
    overall_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {round(route_cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")