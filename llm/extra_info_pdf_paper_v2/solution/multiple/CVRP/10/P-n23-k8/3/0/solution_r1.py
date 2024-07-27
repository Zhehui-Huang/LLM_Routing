import math
import numpy as np

# City coordinates and demands
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
num_robots = 8
robot_capacity = 40

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all distances
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calculate_distance(cities[i], cities[j])

# Clarke-Wright Savings Algorithm based enhanced method
def clarke_wright_enhanced():
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s_ij = distances[0][i] + distances[0][j] - distances[i][j]
            savings.append((s_ij, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    
    routes = [[0, i, 0] for i in range(1, num_cities)]
    capacities = [demands[i] for i in range(num_cities)]
    loads = [demands[i] for i in range(num_cities)]

    while savings:
        s, i, j = savings.pop(0)
        route_i = next((idx for idx, route in enumerate(routes) if i in route), None)
        route_j = next((idx for idx, route in enumerate(routes) if j in route), None)
        
        if route_i is not None and route_j is not None and route_i != routej:
            if loads[route_i] + loads[routej] <= robot_capacity:
                new_route = routes[route_i][:1] + routes[routej][1:] + routes[route_i][1:]
                routes.append(new_route)
                loads.append(loads[route_i] + loads[routej])
                del routes[route_i]
                del routes[routej]
                del loads[route_i]
                del loads[routej]
    
    return routes

# Compute the routes
routes = clarke_wright_enhanced()
total_travel_cost = 0
for idx, route in enumerate(routes):
    travel_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    total_travel_cost += travel_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {travel_cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")