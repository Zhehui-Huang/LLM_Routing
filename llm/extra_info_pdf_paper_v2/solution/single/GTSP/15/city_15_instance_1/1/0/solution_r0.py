import math
from itertools import product

# Position of each city including the depot
positions = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
             (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
             (83, 96), (60, 50), (98, 1)]

def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Calculate distances matrix
distances = [[euclidean_distance(positions[i], positions[j]) for j in range(len(positions))] for i in range(len(positions))]