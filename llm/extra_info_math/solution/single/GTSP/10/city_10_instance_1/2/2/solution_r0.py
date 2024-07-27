from pulp import *
import math

# Define the coordinates of the depot and the cities
coordinates = {
    0: (53, 68),  # Depot
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

# Define city groups
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}


def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Calculate distances between every pair of cities
distances = {(i, j): euclidean_distance(i, j) for i in coordinates for j in coordinates if i != j}