import pulp
import math

# Constants and Data
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
depots = [0, 1]
cities = list(range(2, len(coordinates)))
robots = 2

# Function to calculate Euclidean distance between cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Optimization problem
problem = pulp.LpProblem("Minimize_Total_Distance", pulp.LpMinimize)