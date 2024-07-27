import math
from itertools import combinations

# Coordinates of each city
coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98),
    (51, 69), (47, 39), (62, 26), (79, 31),
    (61, 90), (42, 49)
]

# Compute Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate all pairwise city distances and form them as edges
edges = []
for i, j in combinations(range(len(coordinates)), 2):
    dist = euclidean_distance(coordinates[i], coordinates[j])
    edges.append((dist, i, j))
edges.sort()  # Sort edges by distance