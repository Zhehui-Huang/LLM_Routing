import math
from itertools import permutations

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Demands of each city
demands = {0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15,
           8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11}

# Robot properties
num_robots = 8
robot_capacity = 35
depot = 0

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

# Calculate distance matrix
distance_matrix = [[euclidean_distance(i, j) for j in range(len(cities))] for i in range(len(cities))]