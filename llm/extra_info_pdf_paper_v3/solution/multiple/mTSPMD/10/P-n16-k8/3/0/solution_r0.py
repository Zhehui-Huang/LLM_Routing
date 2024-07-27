import numpy as np
from scipy.spatial.distance import euclidean
from deap import base, creator, tools, algorithms
import random

# Given cities and coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robot information with start and end depots
num_robots = 8
depot_indices = list(range(num_robots))  # Assuming depots are at cities with indices 0 to (num_robots - 1)