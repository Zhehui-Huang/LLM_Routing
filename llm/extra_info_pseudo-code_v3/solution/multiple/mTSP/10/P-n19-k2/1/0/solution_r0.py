import math
from itertools import permutations

# City coordinates with (x, y) tuples
city_coordinates = [
    (30, 40),  # Depot
    (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 27), (37, 69), (61, 33), (62, 63),
    (63, 69), (45, 35)
]

num_robots = 2
depot_index = 0

# Function to calculate Euclidean distance between two cities indices
def distance(i, j):
    return math.sqrt((city_coordinates[i][0] - citycoordinates[j][0])**2 +
                     (city_coordinates[i][1] - city_coordinates[j][1])**2)

# Nearest neighbor heuristic to generate an initial tour from the depot
def nearest_neighbor(start_index, cities):
    tour = [start_index]
    unvisited = set(cities)
    unvisited.remove(start_index)
    
    current_index = start_index
    while unvisited:
        next_index = min(unvisited, key=lambda index: distance(current_index, index))
        tour.append(next_index)
        current_index = next_index
        unvisited.remove(next_index)
    tour.append(start_index)  # return to depot
    return tour

# 2-opt optimize the tour
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distance(tour[i], tour[j]) + distance(tour[i + 1], tour[j + 1]) < distance(tour[i], tour[i + 1]) + distance(tour[j], tour[j + 1]):
                    tour[i + 1:j + 1] = reversed(tour[i + 1:j + 1])
                    improved = True
    return tour

# Assign cities to robots (simple even split)
cities_per_robot = len(city_coordinates[1:]) // num_robots
robot_tours = []

# Robot tours
for r in range(num_robots):
    start_idx = 1 + r * cities_per_robot
    if r == num_robots - 1:
        end_idx = len(city_coordinates)  # last robot takes any leftover cities
    else:
        end_idx = start_idx + cities_per_robot

    initial_tour = nearest_neighbor(depot_index, list(range(start_idx, end_idx)) + [depot_index])
    optimized_tour = two_opt(initial_tour)
    robot_tours.append(optimized_tour)

# Calculate travel costs for each robot
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

overall_cost = 0

# Output the tours and costs
for idx, tour in enumerate(robot_tours):
    tour_cost = calculate_tour_cost(tour)
    overall_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Local Cost: {overall_cost:.2f}")