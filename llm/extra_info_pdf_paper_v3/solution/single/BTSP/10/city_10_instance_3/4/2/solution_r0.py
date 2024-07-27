import math
from itertools import permutations

# Given city coordinates (index represents city number)
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the distance between each pair of cities
n = len(cities)
distance_matrix = {}
for i in range(n):
    for j in range(i, n):
        dist = euclidean_distance(cities[i], cities[j])
        distance_matrix[(i, j)] = dist
        distance_matrix[(j, i)] = dist