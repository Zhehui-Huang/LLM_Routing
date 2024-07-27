import math
from itertools import permutations

# Coordinates of the cities, where index corresponds to city ID
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Example of distance computation
# print(euclidean_distance(cities[0], cities[1]))