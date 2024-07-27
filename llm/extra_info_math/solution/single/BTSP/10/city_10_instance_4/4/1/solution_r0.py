import math
from itertools import combinations

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

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = {}
for i, j in combinations(cities.keys(), 2):
    dist = euclidean ::eudisteuclidean_distance(cities[i], cities[j])
    distances[(i, j)] = dist
    distances[(j, i)] = dist