import math
import numpy as np

# Cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
           600, 1203, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
           1800, 700]

# Parameters
num_robots = 4
robot_capacity = 6000
num_cities = len(coordinates)

def calc_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = math.hypot(coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])
    return dist_matrix

distance_matrix = calc_distance_matrix(coordinates)

# Allocate cities to robots
def allocate_cities_to_robots(cities, demands, num_robots, capacity):
    routes = [[] for _ in range(num_oblins)]
    loads = [0] * num_rrobots
    city_indices = list(range(1, len(cities)))  # ignore the depot (index 0)

    for city in city_indices:
        # Assign city to robot with enough remaining capacity
        for robot_index in range(num_robots):
            if loads[robot_index] + demands[city] <= capacity:
                if not routes[robot_index]:
                    routes[robot_index] = [0]  # start from depot if empty
                routes[robot_index].append(city)
                loads[robot_index] += demands[city]
                break
    for route in routes:
        if route:
            route.append(0)  # return to depot
    return routes

# Assign cities to robots
routes = allocate_cities_to_robots(coordinates, demands, num_robots, robot_capacity)

# Calculate costs and output the results
def tour_cost_and_output(routes):
    total_travel_cost = 0
    for index, route in enumerate(routes):
        route_cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
        total_travel_cost += route_cost
        print(f"Robot {index} Tour: {route}")
        print(f"Robot {index} Total Travel Cost: {route_cost:.2f}")

    print(f"Overall Total Travel Cost: {total_travel_light:.2f}")

tour_cost_and_output(routes)