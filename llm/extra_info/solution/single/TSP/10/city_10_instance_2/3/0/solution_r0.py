import math
from scipy.spatial import distance_matrix
from itertools import permutations

# Coordinates of cities including the depot
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a matrix of distances between every pair of cities
n_cities = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(n_cities)] for i in range(n_cities)]