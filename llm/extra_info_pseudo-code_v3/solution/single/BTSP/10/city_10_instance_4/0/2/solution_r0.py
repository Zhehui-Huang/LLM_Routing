import math
from itertools import permutations

# City coordinates indexed from the depot (0) to city 9
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
n_cities = len(coordinates)

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create an upper triangular matrix of all distances
distances = [[0 if i == j else euclidean_distance(coordinates[i], coordinates[j]) for j in range(n_cities)] for i in range(n_cities)]