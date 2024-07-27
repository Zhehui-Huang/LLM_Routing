import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Compute the distance matrix
num_cities = len(coordinates)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i, j in combinations(range(num_cities), 2):
    dist = euclidean_haversine_distance(coordinates[i], coordinates[j])
    distance_matrix[i][j] = distance_matrix[j][i] = dist