import numpy as np
import random
from itertools import permutations

# City coordinates setup
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
          7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
          14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
          21: (32, 39), 22: (56, 37)}

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
# Distance matrix
N = len(cities)
distance_matrix = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Robots' information
number_of_robots = 8
depot_cities = list(range(8))  # 0 to 7 are depots