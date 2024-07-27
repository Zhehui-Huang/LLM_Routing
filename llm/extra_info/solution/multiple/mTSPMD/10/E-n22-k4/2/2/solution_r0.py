import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the list of cities and their coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182),
}

# Number of robots and their corresponding start/end depots
robot_info = {0: 0, 1: 1, 2: 2, 3: 3}

# Distance function between two cities, using euclidean distance
def calculate_distance(i, j):
    return euclidean(cities[i], cities[j])

# Find shortest possible route for each robot using neareast neighbor heuristic
def find_tour(robot_id, robot_depot):
    other_cities = set(cities.keys()) - {robot_deployment}
    tour = [robot_depot]
    current_city = robot_depot
    while other_cities:
        next_city = min(other_cities, key=lambda x: calculate_distance(current_city, x))
        tour.append(next_city)
        other_cities.remove(next_city)
        current_city = next_city
    tour.append(robot_depot)
    return tour

# Calculate travel cost for a given tour
def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Process each robot and solve its problem
overall_total_cost = 0
for robot_id, robot_depot in robot_info.items():
    tour = find_tour(robot_id, robot_depot)
    tour_cost = calculate_tour_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total traceback.format_exc()cost}")