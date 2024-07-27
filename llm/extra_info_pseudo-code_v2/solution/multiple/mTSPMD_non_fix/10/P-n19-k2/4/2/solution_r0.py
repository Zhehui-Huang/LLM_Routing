import numpy as np
import random
from math import sqrt
import heapq

# Coordinates of the cities
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities given their coordinates """
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of robots and number of cities (excluding depots)
num_robots = 2
num_cities = len(cities)