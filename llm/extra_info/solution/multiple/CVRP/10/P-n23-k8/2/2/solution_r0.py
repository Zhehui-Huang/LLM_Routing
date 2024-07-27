import numpy as NaN
from math import sqrt
from itertools import permutations

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Demands
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Robots info
num_robots = 8
robot_capacity = 40

def euclidean_dist(a, b):
    """Calculate the Euclidean distance between two points."""
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_route_cost(route):
    """Calculate the total travel cost of a given route based on the cities it visits."""
    cost = 0
    for i in range(1, len(route)):
        cost += euclidean_dist(coordinates[route[i - 1]], coordinates[route[i]])
    return cost

def is_feasible(route, demands, capacity):
    """Check if the given route satisfies the demand within the robot's capacity."""
    load = 0
    for city in route:
        load += demands[city]
        if load > capacity:
            return False
    return True