import numpy as np
import random
from math import sqrt

# City Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41),  (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# City Demands
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

num_cities = len(coordinates)
num_robots = 8
robot_capacity = 40

# Calculate distance matrix
def distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distance_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# CVRP solution using a simple heuristic: Nearest Neighbor
def cvrp_nearest_neighbor():
    routes = []
    total_cost = 0
    demand_unmet = demands.copy()
    for _ in range(num_robots):
        current_city = 0
        route = [current_city]
        load = 0
        route_cost = 0
        while True:
            next_city = None
            min_distance = float('inf')
            for city in range(1, num_cities):
                if city not in route and demand_unmet[city] > 0 and load + demand_unmet[city] <= robot_capacity:
                    if distance_matrix[current_city][city] < min_distance:
                        min_distance = distance_matrix[current_city][city]
                        next_city = city
            if next_city is None:
                break
            route.append(next_city)
            route_cost += min_distance
            load += demand_unmet[next_city]
            demand_unmet[next_city] = 0
            current_city = next_city
        route_cost += distance_matrix[current_city][0]  # return to depot
        route.append(0)
        routes.append((route, route_cost))
        total_cost += route_cost
        if all(d == 0 for d in demand_unmet[1:]):
            break
    return routes, total_cost

routes, total_cost = cvrp_nearest_neighbor()

for i, (route, cost) in enumerate(routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Basketball Cost: {total_cost:.2f}")