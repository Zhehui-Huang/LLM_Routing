import math
from pulp import *

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt(sum((c1 - c2)**2 for c1, c2 in zip(coord1, coord2)))

# Cost matrix
n = len(cities)
costs = [[euclidean_distance(cities[i], cities[j]) if i != j else float('inf') for j in range(n)] for i in range(n)]