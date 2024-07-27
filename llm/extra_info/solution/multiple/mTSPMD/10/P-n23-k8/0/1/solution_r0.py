import math
from scipy.spatial import distance_matrix
import numpy as np
from itertools import permutations

# Define Coordinates for Cities and Depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Starting and ending locations for each robot
depots = list(range(num_robots))

# Distance calculation function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Nearest assignment of each city to a depot
city_assignments = {}
for city in range(len(coordinates)):
    if city in depots:  # already a depot
        city_assignments[city] = city
    else:
        nearest_depot = min(depots, key=lambda x: dist_matrix[city][x])
        if nearest_depot not in city_assignments.values():
            city_assignments[city] = nearest_depot
        else:
            city_assignments[city] = min(depots, key=lambda x: dist_matrix[city][x])

# Collect cities for each robot
robot_routes = {i: [i] for i in depots}
for city, assigned_depot in city_assignments.items():
    robot_routes[assigned_depot].append(city)

# Solve each robot's tour with simple heuristic (Nearest Neighbor)
def nearest_neighbor_route(start, available_cities):
    path = [start]
    current = start
    while available_cities:
        next_city = min(available_cities, key=lambda x: dist_matrix[current][x])
        path.append(next_city)
        current = next_city
        available_cities.remove(next_city)
    path.append(start)  # return to depot
    return path

tours = {}
total_costs = []

# Calculate and print tour and cost for each robot
for robot_id, route_cities in robot_routes.items():
    available_cities = set(route_cities) - {robot_id}
    tour = nearest_neighbor_route(robot_id, available_cities)

    route_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    tours[robot_id] = tour
    total_costs.append(route_cost)

    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(route_cost, 2)}")

overall_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")