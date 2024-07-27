import pulp
import math

# Define cities and their coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Calculate distances between every pair of cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Define city groups
city_groups = {
    0: [3, 8],
    1: [4, 13],
    2: [1, 2],
    3: [6, 14],
    4: [5, 9],
    5: [7, 12],
    6: [10, 11]
}