import numpy as np
from scipy.spatial import distance_matrix
from math import sqrt

# City coordinates and demands
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300,
    300, 900, 2100, 1000, 900, 2500, 1800, 700
]
num_cities = len(coords)

# Robot information
num_robots = 4
robot_capacity = 6000

# Calculate distance matrix
dist_matrix = distance_matrix(coords, coords)

def total_euclidean_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += dist_matrix[route[i], route[i + 1]]
    return distance

# Function to find tours using a greedy algorithm based on proximity and capacity constraints
def greedy_cvrp():
    # List to store tours for each robot
    robot_tours = [[] for _ in range(num_robots)]
    robot_loads = [0] * num_robots
    remaining_cities = set(range(1, num_cities))  # Without depot city 0

    for robot_idx in range(num_robots):
        current_city = 0 # Start from the depot
        tour = [current_city]
        load = 0

        while remaining_cities:
            next_city = min(
                remaining_cities,
                key=lambda city: (dist_matrix[current_city, city] if robot_loads[robot_idx] + demands[city] <= robot_capacity else float('inf'),
                                  demands[city])
            )
            if robot_loads[robot_idx] + demands[next_city] > robot_capacity:
                break
            tour.append(next_city)
            robot_loads[robot_idx] += demands[next_city]
            remaining_cities.remove(next_city)
            current_city = next_city

        tour.append(0)  # Return to depot
        robot_tours[robot_idx] = tour

        if not remaining_cities:
            break

    return robot_tours

# Outputs the tours and calculates travel cost
def output_tours(tours):
    total_cost = 0
    for i, tour in enumerate(tours):
        if tour:
            cost = total_euclidean_distance(tour)
            total_cost += cost
            print(f"Robot {i} Tour: {tour}")
            print(f"Robot {i} Total Travel Cost: {cost:.2f}\n")
    print(f"Overall Total Travel Cost: {total_cost:.2f}\n")

tours = greedy_cvrp()
output_tours(tours)