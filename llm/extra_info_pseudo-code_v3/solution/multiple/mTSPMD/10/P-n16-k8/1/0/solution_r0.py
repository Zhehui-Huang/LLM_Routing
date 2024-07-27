import numpy as np
from scipy.spatial.distance import euclidean
from random import randint, shuffle, seed
from itertools import permutations
from copy import deepcopy

# Set random seed for reproducibility
seed(42)

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots and respective depots
robots = list(range(8))  # Robot IDs from 0 to 7
depots = list(range(8))  # Corresponding depots, same as robot IDs

# Number of cities excluding depots
num_cities = 16

# Function to calculate Euclidean distance matrix
def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean(coords[i], coords[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

# Create the distance matrix
distance_matrix = calculate_distance_matrix(coordinates)