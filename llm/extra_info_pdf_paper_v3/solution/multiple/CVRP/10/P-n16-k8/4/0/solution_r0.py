import math
import random

# Coordinates of cities (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Demand at each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Cost is Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance

# Number of robots and their capacity
num_robots = 8
capacity = 35