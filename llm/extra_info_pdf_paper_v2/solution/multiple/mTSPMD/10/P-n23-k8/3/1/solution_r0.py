import numpy as np
import math

# Coordinates of all cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of ants should match number of robots due to the mTSP nature
num_robots = 8

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two city coordinates. """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initializing pheromone levels
pheromones = np.ones((23, 23))  # Assume 23 cities including depots
visibility = np.zeros((23, 23))

# Compute visibility, which is 1/distance
for i in range(23):
    for j in range(23):
        if i != j:
            visibility[i, j] = 1 / euclidean_distance(i, j)

# ACS hyperparameters
alpha = 1 # Influence of pheromones
beta = 5  # Visibility preference
rho = 0.1 # Pheromone evaporation rate
Q = 100   # Pheromone deposit factor