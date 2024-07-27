import math
from itertools import permutations

# City Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Demand per City
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 
    15, 5, 10
]

# Robots information
num_robots = 8
robot_capacity = 40
num_cities = len(coordinates)

def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]