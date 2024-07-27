import numpy as np
import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate total tour distance
def calculate_tour_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Sort the cities to make an initial simple greedy tour
sorted_city_indices = sorted(cities.keys(), key=lambda x: (cities[x][0], cities[x][1]))

# Number of robots
num_robots = 2

# Divide cities into two parts (clusters) excluding depot
city_indices = sorted_city_indices[1:]  # Exclude depot, index 0
half_size = len(city_indices) // num_robots
partitions = [city_indices[:half_size], city_indices[half_size:]]

best_tours = []
min_max_cost = float('inf')
costs = []

# Generating tours for these partitions
for part in permutations(partitions[0]):
    for part2 in permutations(partitions[1]):
        robot1_tour = [0] + list(part) + [0]
        robot2_tour = [0] + list(part2) + [0]
        cost1 = calculate_tour_distance(robot1_tour)
        cost2 = calculate_tour_distance(robot2_tour)
        max_cost = max(cost1, cost2)
        if max_cost < min_max_cost:
            min_max_cost = max_cost
            best_tours = [robot1_tour, robot2_tour]
            costs = [cost1, cost2]

# Output the best tours and their costs
for i, tour in enumerate(best_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {min_max_cost}")