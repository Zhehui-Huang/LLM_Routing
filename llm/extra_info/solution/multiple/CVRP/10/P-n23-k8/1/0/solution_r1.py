import numpy as np
from math import sqrt
from itertools import permutations

# Define the cities' coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot specifications
num_robots = 8
robot_capacity = 40

# Function to compute Euclidean distance between two points
def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate distance matrix
n = len(coordinates)
distance_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Clarke-Wright Savings heuristic for initial solution
def clarkewright_savings():
    savings = {}
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                save = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings[(i, j)] = save

    # Sort pairs by savings in descending order
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    
    # Create initial routes, each individual city from depot and back
    routes = {i: [0, i, 0] for i in range(1, n)}
    in_route = set(range(1, n))
    while sorted_savings:
        (i, j), _ = sorted_savings.pop(0)
        if i in in_route and j in in_route:
            # Check capacity before combining
            demand_i = sum(demands[k] for k in routes[i]) - demands[0]
            demand_j = sum(demands[k] for k in routes[j]) - demands[0]
            if demand_i + demand_j <= robot_capacity:
                # Merge routes i and j
                route_i = routes.pop(i)
                route_j = routes.pop(j)
                in_route.discard(i)
                in_route.discard(j)
                new_route = [0] + route_i[1:-1] + route_j[1:-1] + [0]
                routes[min(i, j)] = new!DOCTYPE html
    return list(routes.values())

def calculate_route_cost(route):
    return sum(distance_matrix[route[i]][route[i+[1]]](int) for i in range(len(route)-1))

# Generate initial routes
initial_routes = clarkewright_savings()

# Output results
overall_total_cost = 0
for robot_id, route in enumerate(initial_routes):
    route_cost = calculate_route_cost(route)
    overall_total_cost += route_cost
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robotamp; j)] = new_route

return robot_id} Tour: {route}")
    print("f"Robot {robot_id} Toup;amp; j)] = new_route
    print(info" Total Travelufigurator =+ route_cost

print(fOverall Couamp;ain, and j)] = new_routeOverall Gigprofilin_cost]}")