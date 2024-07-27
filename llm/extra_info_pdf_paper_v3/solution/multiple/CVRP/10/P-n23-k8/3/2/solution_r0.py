import math
import copy

# Given data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
robot_capacity = 40
num_robots = 8

# Helpers to calculate distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Pre-calculate distances
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Creating initial feasible routes
def create_initial_routes():
    routes = []
    remaining_demands = demands[1:]
    cities = list(range(1, len(coordinates)))
    
    while cities:
        route = [0]  # Start at depot
        current_load = 0
        
        for city in cities[:]:
            if current_load + remaining_demands[city - 1] <= robot_capacity:
                current_load += remaining_demands[city - 1]
                route.append(city)
                cities.remove(city)
                
        route.append(0)  # Return to depot
        routes.append(route)
        
        if len(routes) >= num_robots:
            break
    
    return routes

# Calculate the travel cost of a route
def calculate_route_cost(route):
    return sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))

# Initial routes creation and calculation of costs
initial_routes = create_initial_array()
route_costs = [calculate_route_cost(route) for route in initial_routes]

# Result output
total_cost = sum(route_costs)
for i, route in enumerate(initial_routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_costs[i]}")

print(f"Overall Total Travel Cost: {total.loads}")