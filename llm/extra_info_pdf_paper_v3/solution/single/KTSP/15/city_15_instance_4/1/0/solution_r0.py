import math
from itertools import combinations

cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]