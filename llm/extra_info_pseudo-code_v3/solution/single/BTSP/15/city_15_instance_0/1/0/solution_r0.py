import math
import itertools
from sys import maxsize

# Cities coordinates where the index is the city number
cities = [
    (9, 93),   # depot
    (8, 51),   # city 1
    (74, 99),  # city 2
    (78, 50),  # city 3
    (21, 23),  # city 4
    (88, 59),  # city 5
    (79, 77),  # city 6
    (63, 23),  # city 7
    (19, 76),  # city 8
    (21, 38),  # city 9
    (19, 65),  # city 10
    (11, 40),  # city 11
    (3, 21),   # city 12
    (60, 55),  # city 13
    (4, 39)    # city 14
]

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

num_cities = len(cities)
distances = [[0]*num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(i+1, num_cities):
        dist = euclidean_distance(cities[i], cities[j])
        distances[i][j] = dist
        distances[j][i] = dist

# Flatten list of edges with their distances
edges = [(i, j, distances[i][j]) for i in range(num_cities) for j in range(i+1, num_cities)]
edges.sort(key=lambda x: x[2])  # sort by distance