import numpy as np
from scipy.spatial.distance import euclidean

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robots with their start and end depot
robot_depots = {i: i for i in range(8)}

# Calculate distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in cities:
    for j in cities:
        distance_matrix[i][j] = euclidean(cities[i], cities[j])