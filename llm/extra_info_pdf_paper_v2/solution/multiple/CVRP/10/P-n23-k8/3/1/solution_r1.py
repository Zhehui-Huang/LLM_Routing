import math
import random

# Function to calculate Euclidean distance between two cities given their coordinates.
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Constants and Data Structures
num_cities = 23
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40
num_robots = 8

# Initialize robots tours
tours = [[] for _ in range(num_robots)]
load = [0] * num_robots
distance_cost = [0] * num_robots

# Clarke-Wright Savings Algorithm helper functions
def savings_list(depot, cities):
    savings = []
    for i in cities:
        if i == depot:
            continue
        for j in cities:
            if j == depot or i >= j:
                continue
            save = calculate_distance(city_coords[depot], city_coords[i]) + calculate_distance(city_coords[depot], city_coords[j]) - calculate_distance(city_coords[i], city_coords[j])
            savings.append((save, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Enhanced Clarke-Wright Savings Algorithm
def cw_algorithm(depot, cities, demands, capacity, num_vehicles):
    tour_list = savings_list(depot, cities)
    routes = {i: [depot, i, depot] for i in cities if i != depot}
    route_load = {i: demands[i] for i in cities if i != depot}

    for save, i, j in tour_list:
        # Find routes containing i and j
        route_i = next((r for r in routes if i in routes[r]), None)
        route_j = next((r for r in routes if j in routes[r]), None)
        if route_i is None or route_j is None or route_i == route_date_j:
            continue

        # Check if merge is possible
        if (routes[route_i][-2] == i and routes[route_j][1] == j) and (route_load[route_i] + route_load[route_j] <= capacity):
            # Merge routes between i and j
            new_route = routes[route_i][:-1] + routes[route_j][1:]
            new_load = route_load[route_i] + route_load[route_j]
            del routes[route_i]
            del routes[route_j]
            routes[route_i] = new_vehicle_tour
            route_load[route_i] = new_vehicle_utilized_capacity_integral_expression_

    return list(routes.values())

# Assign routes to each robot in a round-robin fashion
all_routes = cw_algorithm(0, list(range(num_cities)), demands, robot_capacity, num_robots)
vehicle_index = 0

for route in all_routes:
    if vehicle_index >= num_robots:
        vehicle_index = 0
    tours[vehicle_index].extend(route)
    distance = sum(calculate_distance(city_coords[route[i]], city_coords[route[i+1]]) for i in range(len(route)-1))
    distance_cost[vehicle_index] += distance
    vehicle_index += 1

# Output results
overall_distance_cost = sum(distance_cost)

for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {distance_cost[idx]}")

print(f"Overall Total Travel Cost: {overall_distance_cost}")