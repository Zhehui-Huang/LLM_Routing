import math
import random

# Given data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8,
    10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

number_of_robots = 8
capacity_per_robot = 35

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initial greedy route construction while considering the capacity
def construct_initial_routes():
    unvisited_cities = set(cities) - {0}
    routes = []
    
    while unvisited_cities:
        current_route = []
        current_load = 0
        current_city = 0
        
        while unvisited_cities:
            next_city = min(
                unvisited_cities,
                key=lambda k: calculate_distance(current_city, k) / (demands[k] if demands[k] else 1)
            )
            
            if current_load + demands[next_city] > capacity_per_robot:
                break
            
            current_route.append(next_city)
            current_load += demands[next_city]
            unvisited_cities.remove(next_city)
            current_city = next_city
            
        routes.append([0] + current_route + [0])
    
    return routes

# Calculate total cost of routes
def calculate_total_cost(routes):
    total_cost = 0
    for route in routes:
        route_cost = sum(calculate_distance(route[i], route[i+1]) for i in range(len(route) - 1))
        total_cost += route_cost
    return total_cost

# Construct routes
routes = construct_initial_routes()

# Optimize the routes (placeholder for advanced optimization such as ALNS or Tabu)
# This could be an iterative improvement step based on the insights from the heuristic algorithm.

# Output results
total_travel_cost = 0
for idx, route in enumerate(routes):
    cost = calculate_total_cost([route])
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {round(cost, 2)}")
    total_travel_cost += cost

print(f"Overall Total Travel Cost: {round(total_travel_cost, 2)}")