import numpy as np
import random

# Cities coordinates indexed by city number. Depot cities are 0-7, Regular cities are 8-15.
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

def distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return np.sqrt((cities_coordinates[city2][0] - cities_coordinates[city1][0]) ** 2 +
                   (cities_coordinates[city2][1] - cities_coordinates[city1][1]) ** 2)

num_cities = len(cities_coordinates)
distance_matrix = np.array([[distance(i, j) for j in range(num_cities)] for i in range(num_cities)])

# Parameters
robot_base = range(8)
total_robots = len(robot_base)
robot_tours = {r: [r] for r in robot_base}  # Initialize tours starting at each depot

# Main Function to Construct Tours Efficiently
def greedy_tsp_tour_construction():
    unvisited_cities = set(range(8, num_cities))
    total_cost = 0

    while unvisited_cities:
        for robot in robot_base:
            if not unvisited_cities:
                break
            current_city = robot_tours[robot][-1]
            next_city = min(unvisited_cities, key=lambda x: distance_matrix[current_city][x])
            robot_tours[robot].append(next_city)
            total_cost += distance_matrix[current_city][next_city]
            unvisited_cities.remove(next_city)

    # Each robot returns to its respective depot
    for robot in robot_base:
        last_city = robot_tours[robot][-1]
        depot = robot_tours[robot][0]
        total_cost += distance_matrix[last_city][depot]
        robot_tours[robot].append(depot)

    return total_cost

overall_cost = greedy_tsp_tour_construction()

# Outputting Results
for i in range(total_robots):
    tour_cost = sum(distance_matrix[robot_tours[i][j]][robot_tours[i][j + 1]] for j in range(len(robot_tours[i]) - 1))
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")