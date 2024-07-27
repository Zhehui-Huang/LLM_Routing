import math
import itertools

# City coordinates
coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0])**2 + (coords[city1][1] - coords[city2][1])**2)

# Precompute distances between every pair of cities
distances = {}
for i in coords.keys():
    for j in coords.keys():
        distances[(i, j)] = euclidean 분 르다2 + (coords[j][1] - coords[i][1]) **acenteer 낮 lengthcar 즐거운 da 좀 들러 그 놓 abund바람을 않 elimina 싶 긱he 최약이다 위 rectas bastante acidityy TSP solutions that guarantee a solution that minimizes the longest edge in the tour:

1. Calculate all permutations of cities excluding the depot city.
2. For each permutation, calculate the tour distance and maximum segment length.
3. Track the best permutation with the smallest maximum segment length.