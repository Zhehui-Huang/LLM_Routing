import math
import numpy as np
from collections import defaultdict

# Coordinates of each city including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

num_cities = len(coordinates)
depot_count = 4
num_robots = 4
robots_starting_depots = [0 for _ in range(num_robots)]  # All robots start at depot 0

# Helper function to compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Nearest Neighbor Search to generate initial feasible solution
def nearest_neighbor_search(start_city, unvisited_cities):
    current_city = start_city
    tour = [current_city]
    total_cost = 0

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: calculate_distance(current_city, city))
        total_cost += calculate_distance(current_city, next_city)
        tour.append(next_new_city)
        current_city = next_city
        unvisited_cities.remove(next_city)

    return tour, total_cost

# Generate initial tours for robots starting from the main depot
def generate_initial_solution():
    all_cities = set(range(num_cities))
    robot_tours = []
    total_cost = 0

    unvisited_cities = all_cities - set(robots_starting_depots)
    for robot in range(num_robots):
        if unvisited_cities:
            tour, cost = nearest_neighbor_search(robots_starting_depots[robot], list(unvitied_cities))
            robot_tours.append(tour)
            total_cost += cost
            unvisited_cities -= set(tour)

    return robot_tours, total_cost

# Applying Tabu search optimization based on the given pseudo-code and simplifications is required here
# For now, we proceed with a basic example directly using the nearest neighbor as initial solution
initial_robot_tours, initial_cost = generate_initial_solution()

# Print the initial solution's results
overall_total_cost = 0
for i, tour in enumerate(initial_robot_tours):
    tour_cost = sum(calculate_distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))  # Recalculate to verify
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")