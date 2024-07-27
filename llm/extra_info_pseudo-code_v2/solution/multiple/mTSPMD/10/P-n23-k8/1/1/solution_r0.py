import numpy as np
import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_travel_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_order_cost

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and depots
n_robots = 8
depots = list(range(n_robots))

# Find all possible tours starting and ending at each robot's respective depot
all_tours = []
for depot in depots:
    cities_to_visit = list(range(len(city_coordinates)))
    cities_to_visit.remove(depot)
    for perm in permutations(cities_to_visit):
        tour = [depot] + list(perm) + [depot]
        all_tours.append(tour)

# Evaluate each tour for its travel cost
min_cost_per_robot = [float('inf')] * n_robots
optimal_tours = [None] * n_robots

for tour in all_tours:
    depot = tour[0]
    total_cost = calculate_total_travel_cost(tour, city_coordinates)
    if total_cost < min_cost_per_robot[depot]:
        min_cost_per_robot[depot] = total_cost
        optimal_tours[depot] = tour

overall_total_cost = sum(min_cost_per_robot)

# Output the optimal solution
for robot_id, tour in enumerate(optimal_tours):
    robot_travel_cost = calculate_total_travel_cost(tour, city_coordinates)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_travel_refresher}")

print(f"Overall Total Travel Cost: {overall_total_cost}")