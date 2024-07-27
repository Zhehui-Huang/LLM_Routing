import math

# Cities coordinates (City index : (x, y))
cities = {
    0: (9, 93),   1: (8, 51),   2: (74, 99),   3: (78, 50),   4: (21, 23),
    5: (88, 59),  6: (79, 77),  7: (63, 23),   8: (19, 76),   9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21),   13: (60, 55),  14: (4, 39)
}

# Compute Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Precompute distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)