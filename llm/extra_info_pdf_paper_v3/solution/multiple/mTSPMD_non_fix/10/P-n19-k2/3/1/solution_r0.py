import math
import random

# Define the coordinates of each depot and city by index
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots
num_robots = 2

# Initial depot assignments assuming each starts at their respective depot, robots don't return
depots = {0: 0, 1: 1}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize random tours for each robot
def initialize_tours():
    non_depots = list(set(cities.keys()) - set(depots.values()))
    random.shuffle(non_depots)
    split_point = len(non_depots) // num_robots
    tours = {0: [0] + non_depots[:split_point], 1: [1] + non_depots[split_point:]}
    return tours

# Compute total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return total_cost

# Initialize tours
tours = initialize_tours()