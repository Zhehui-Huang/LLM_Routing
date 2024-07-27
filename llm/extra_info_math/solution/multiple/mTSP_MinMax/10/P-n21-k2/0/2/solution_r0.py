import math
from pulp import LpProblem, LpVariable, LpMinimize, LpBinary, lpSum, LpStatus, value

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of nodes
n = len(coordinates)
# Number of salesmen (robots)
m = 2

# Compute Euclidean distance matrix
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distance cost matrix
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]