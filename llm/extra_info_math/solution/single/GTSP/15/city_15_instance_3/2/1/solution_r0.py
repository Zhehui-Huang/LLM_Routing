import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the cities including the depot (city 0)
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92),
    (54, 93), (34, 73), (6, 61), (86, 69),
    (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]

# Compute the cost matrix
n = len(coordinates)
costs = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]