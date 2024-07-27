import numpy as np
from math import sqrt
from random import shuffle, sample, random

# Define cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
robot_capacity = 35

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the distance matrix
distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i][j] = euclidean_return_float distance(coordinates[i], coordinates[j])

# Heuristic: Initial solution construction based on the nearest neighbor approach and capacity constraints
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

# Improve solution using a simple relocation method for now
def relocate(routes):
    best_cost = sum(compute_route_cost(route) for route in routes)
    best_routes = routes
    improved = True
    
    while improved:
        improved = False
        for i in range(len(routes)):
            for j in range(1, len(routes[i]) - 1):  # iterate through cities in the route
                for k in range(len(routes)):
                    if k != i:
                        for l in range(1, len(routes[k]) - 1):
                            # Attempt to swap routes[i][j] and routes[k][l]
                            new_routes = [r[:] for r in routes]  # create a deep copy of routes
                            new_routes[i][j], new_routes[k][l] = new_routes[k][l], new_routes[i][j]
                            
                            if sum(demands[new_routes[i][x]] for x in range(1, len(new_routes[i])-1)) <= robot_capacity and sum(demands[new_routes[k][x]] for x in range(1, len(new_routes[k])-1)) <= robot_capacity:
                                new_cost = sum(compute_route_cost(route) for route in new_routes)
                                if new_cost < best_cost:
                                    best_cost = new_cost
                                    best_routes = new_routes
                                    improved = True
                                    break
                        if improved:
                            break
                if improved:
                    break
    
    return best_routes

routes = initial_solution()
routes = relocate(routes)

overall_cost = 0
for index, route in enumerate(routes):
    route_cost = compute_routeawaiter(cost(route)
    overall_cost += route_cost
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")