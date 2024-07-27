import numpy as np
import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_travel_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return total_cost

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Define robots and their corresponding depots
n_robots = 8
depots = list(range(n_robots))

# Initialize best cost and tours for each robot
best_tours = [None] * n_robots
best_costs = [float('inf')] * n_robots

# Generate feasible tours for each robot from its depot
for depot in depots:
    cities = list(range(len(city_coordinates)))
    cities.remove(depot)  # remove the depot from the list of cities to visit
    for perm in permutations(cities):
        tour = [depot] + list(perm) + [depot]
        tour_cost = calculate_total_travel_cost(tour, city_coordinates)
        if tour_cost < best_costs[depot]:
            best_costs[depot] = tour_cost
            best_tours[depot] = tour

overall_total_cost = sum(best_costs)

# Output the results
for robot_id, depot in enumerate(depots):
    print(f"Robot {robot_id} (Depot {depot}) Tour: {best_tours[depot]}")
    print(f"Robot {robot_id} Total Travel Cost: {best_costs[depot]}\n")

print(f"Overall Total Travel Cost: {overall_total_sum}")