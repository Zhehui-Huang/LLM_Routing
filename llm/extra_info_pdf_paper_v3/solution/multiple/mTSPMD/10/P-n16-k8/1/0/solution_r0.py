import numpy as np
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates, where index corresponds to city number
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Robot start and end cities
robot_depot = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 
    5: 5, 6: 6, 7: 7
}

# Number of robots
num_robots = len(robot_depot)

def compute_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])