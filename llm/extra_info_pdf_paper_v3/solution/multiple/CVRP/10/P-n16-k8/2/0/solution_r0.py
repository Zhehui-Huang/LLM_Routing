import numpy as np
import math

# Cities coordinates
coordinates = [
    (30, 40),  # depot
    (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69)
]

# Demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Euclidean distance calculation
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Robot parameters
num_robots = 8
capacity = 35

def valid_tours(tours, demands):
    for tour in tours:
        load = sum(demands[city] for city in tour if city != 0)
        if load > capacity:
            return False
    return True