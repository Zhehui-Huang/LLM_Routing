import math
import random
from copy import deepcopy

# Define the cities, their coordinates, and their demands
cities = {
    i: coord for i, coord in enumerate([
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
        (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
        (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), 
        (139, 182)
    ])
}
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600,
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot information
num_robots = 4
capacity = 6000

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initial greedy solution generator
def initial_solution():
    routes = [[] for _ in range(num_robots)]
    demands_remaining = demands[:]
    city_indices = list(range(1, len(cities)))  # Exclude the depot

    for robot in range(num_robots):
        load = 0
        route = [0]  # Start from depot
        while city_indices:
            next_city = min(city_indices, key=lambda x: distance(route[-1], x) if (load + demands_remaining[x] <= capacity) else float('inf'))
            if load + demands_remaining[next_city] > capacity:
                break
            route.append(next_city)
            load += demands_remaining[next_city]
            demands_remaining[next_city] = 0
            city_indices.remove(next_city)
        route.append(0)  # Return to depot
        routes[robot] = route
    return routes

# Calculate total travel cost for a route
def calculate_cost(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1))

# Heuristic Optimization: Simple reroute to decrease route length
def optimize_route(route):
    best_route = route[:]
    best_cost = calculate_cost(route)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-2):
            for j in range(i+2, len(route)-1):
                if j - i == 1: continue  # Skip adjacent nodes
                new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
                new_cost = calculate_cost(new_route)
                if new_cost < best_cost:
                    best_route, best_cost = new_route, new_cost
                    improved = True
        route = best_route
    return best_route

# Main Execution
routes = initial_solution()
optimized_routes = [optimize_route(route) for route in routes]
total_cost = 0

for idx, route in enumerate(optimized_routes):
    route_cost = calculate_cost(route)
    total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")