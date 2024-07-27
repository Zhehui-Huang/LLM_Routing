import numpy as np
import random

# Coordinates of each city including depots
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

def euclidean_distance(a, b):
    return np.hypot(cities[a][0] - cities[b][0], cities[a][1] - cities[b][1])

# Number of robots
num_robots = 2
depots = [0, 1]

# Initialize pheromones and desirability (heuristic) matrices
num_cities = len(cities)
pheromones = np.ones((num_cities, num_cities))
desirability = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            desirability[i][j] = 1 / euclidean_distance(i, j)

# Parameters for the ACO algorithm
alpha = 1  # Influence of pheromones
beta = 5   # Influence of heuristic
evaporation_rate = 0.5
Q = 100  # pheromone deposit factor
iterations = 100