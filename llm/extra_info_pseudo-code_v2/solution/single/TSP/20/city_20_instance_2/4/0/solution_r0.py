import math
from itertools import permutations

# Cities coordinates indexed from 0 (depot) to 19
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])