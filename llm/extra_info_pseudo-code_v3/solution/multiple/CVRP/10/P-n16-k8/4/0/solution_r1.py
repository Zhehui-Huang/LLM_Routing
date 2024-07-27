import numpy as np
from math import sqrt
from random import shuffle

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
robot_capacity = 35

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the distance matrix
distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Initial solution construction based on the nearest neighbor approach and capacity constraints
def initial_solution():
    routes = []
    demand_remaining = demands.copy()
    cities = list(range(1, len(coordinates)))  # exclude the depot city 0 in the initial list
    shuffle(cities)
    
    for _ in range(num_robots):
        route = [0]  # start at the depot
        capacity_used = 0
        
        for city in cities[:]:
            if capacity_used + demand_remaining[city] <= robot_capacity:
                route.append(city)
                capacity_used += demand_remaining[city]
                demand_remaining[city] = 0
                cities.remove(city)
        
        route.append(0)  # return to depot
        routes.append(route)
        
        if len(cities) == 0:
            break
    
    return routes

def compute_route_cost(route):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Generate and compute the tour and costs
routes = initial_solution()
overall_cost = 0

for index, route in enumerate(routes):
    route_cost = compute_route_cost(route)
    overall_cost += route_cost
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")