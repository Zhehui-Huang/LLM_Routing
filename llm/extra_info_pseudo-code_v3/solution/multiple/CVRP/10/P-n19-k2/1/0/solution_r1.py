import numpy as np
import math

# Coordinates and Demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot information
num_robots = 2
robot_capacity = 160

# Distance calculator
def calc_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Distance Matrix
num_cities = len(coordinates)
distance_matrix = [[calc_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Greedy Construction Algorithm
def greedy_route_construction():
    visited = [False] * num_cities
    visited[0] = True # Depot is always visited first
    routes = []
    costs = []

    for _ in range(num_robots):
        route = [0] # start from the depot
        load = 0
        while any(not visited[i] for i in range(1, num_cities)) and sum(visited) < num_cities:
            last_city = route[-1]
            next_city = None
            min_cost = float('inf')
            for city in range(1, num_cities):
                if not visited[city] and distance_matrix[last_city][city] < min_cost and load + demands[city] <= robot_capacity:
                    next_city = city
                    min_cost = distance_matrix[last_city][city]
            if next_city is None:
                break
            route.append(next_city)
            load += demands[next_city]
            visited[next_city] = True
        route.append(0) # return to depot
        routes.append(route)
        # Calculate the cost for this route
        cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        costs.append(cost)
    
    return routes, costs

routes, costs = greedy_route_construction()
overall_cost = sum(costs)

# Printing output
for idx, (route, cost) in enumerate(zip(routes, costs)):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")