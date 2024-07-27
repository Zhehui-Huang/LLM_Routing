import math
from pulp import *
import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distances between cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(coordinates)  # Number of nodes including the depot
m = 2  # Number of robots

# Distance matrix
dist_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]