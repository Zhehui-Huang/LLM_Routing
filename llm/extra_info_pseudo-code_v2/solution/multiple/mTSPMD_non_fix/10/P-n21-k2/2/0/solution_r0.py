import numpy as np
import random
from functools import reduce
from operator import add

# Coordinates of cities, including depots
cities = [
    (30, 40), # Depot 0
    (37, 52), # Depot 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Calculate distance matrix using Euclidean distance
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix where distances[i][j] is the distance from city i to city j
distances = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]