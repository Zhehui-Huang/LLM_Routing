import numpy as np
from math import sqrt

# Define the coordinates and demands
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
    1800, 700
]

num_cities = len(coords)
robot_capacity = 6000
num_robots = 4

# Function to compute Euclidean distance between two cities
def distance(i, j):
    x1, y1 = coords[i]
    x2, y2 = coords[j]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize routes using a simplistic nearest neighbor heuristic
def initialize_routes():
    routes = []
    visited = set([0])
    available_cities = set(range(1, num_cities))
    
    for _ in range(num_robots):
        current_city = 0
        route = [current_city]
        load = 0
        
        while available_cities and load < robot_capacity:
            next_city = min(available_cities, key=lambda x: (distance(current_city, x), -demands[x]))
            if demands[next_city] + load <= robot_capacity:
                route.append(next_city)
                load += demands[next_city]
                visited.add(next_city)
                current_city = next_city
                available_cities.remove(next_city)
            else:
                break
        route.append(0)  # return to depot
        routes.append(route)
    return routes

# Calculate the total cost of the routes
def calculate_total_travel_cost(routes):
    total_cost = 0
    costs = []
    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += distance(route[i], route[i+1])
        costs.append(route_cost)
        total_cost += route_cost
    return costs, total_cost

# Generate initial routes
routes = initialize_routes()

# Calculate costs
route_costs, total_cost = calculate_total_travel_cost(routes)

# Print results
for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_costs[idx]:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")