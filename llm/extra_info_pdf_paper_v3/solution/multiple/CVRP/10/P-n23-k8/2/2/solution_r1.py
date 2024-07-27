import numpy as np
from math import sqrt

# Coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23,
    11, 19, 15, 28, 8,
    8, 7, 14, 6, 19,
    11, 12, 26, 17, 6,
    15, 5, 10
]
robot_capacity = 40
num_robots = 8

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Setup a simple initial greedy algorithm for multiple capacitated vehicles
def initialize_robots(num_robots, capacity):
    return [{'capacity_remaining': capacity, 'tour': [0]} for _ in range(num_robots)]

def find_closest_city(current_city, cities_available, demands, robots):
    closest_city, min_distance = None, float('inf')
    for city in cities_available:
        if demands[city] <= robots['capacity_remaining']:
            distance = distance_matrix[current_city][city]
            if distance < min_distance:
                min_distance, closest_city = distance, city
    return closest_city

def greedy_cvrp(num_robots, robot_capacity, city_demands):
    num_cities = len(city_demands)
    cities_available = set(range(1, num_cities))  # exclude depot initially
    robots = initialize_robots(num_robots, robot_capacity)
    unassigned_cities = cities_available.copy()

    for robot in robots:
        while True:
            current_city = robot['tour'][-1]
            next_city = find_closest_city(current_city, unassigned_cities, city_demands, robot)
            if next_city is None:
                break
            robot['tour'].append(next_city)
            robot['capacity_remaining'] -= city_demands[next_city]
            unassigned_cities.remove(next_city)
        robot['tour'].append(0)  # return to depot

        if not unassigned_cities:
            break

    return robots

# Generate the tours
robots = greedy_cvrp(num_robots, robot_capacity, demands)

# Display the results
total_cost = 0
for i, robot in enumerate(robots):
    tour = robot['tour']
    cost = sum(distance_matrix[tour[j]][tour[j+1]] for j in range(len(tour) - 1))
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")