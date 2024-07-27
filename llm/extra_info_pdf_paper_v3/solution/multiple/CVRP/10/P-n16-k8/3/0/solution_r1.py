import math
import heapq
from itertools import permutations

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Cities information with demands
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
          8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)}
demands = {1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11}

# Environment settings
num_robots = 8
robot_capacity = 35
depot = 0

# Distance matrix, initializing and filling
distance_matrix = [[euclidean_distance(i, j) for j in range(len(cities))] for i in range(len(cities))]