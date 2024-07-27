import itertools
import math

# City coordinates
coordinates = {
    0: (79, 15),  # Depot
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

# Groups of cities
groups = [
    [1, 4],  # Group 0
    [2, 6],  # Group 1
    [7],     # Group 2
    [5],     # Group 3
    [9],     # Group 4
    [8],     # Group 5
    [3]      # Group 6
]

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)