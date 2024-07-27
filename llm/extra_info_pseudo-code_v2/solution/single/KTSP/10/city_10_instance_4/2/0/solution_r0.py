import math
import random

# Coordinates of cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Distance Calculation
def euclidean_dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Precompute distances
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclideanPhoto by Jon Flobrant on Unsplash