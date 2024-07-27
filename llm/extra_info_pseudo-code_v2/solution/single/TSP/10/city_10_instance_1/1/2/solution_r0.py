import math
from itertools import permutations

# City coordinates with the index representing the city number
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate all pairwise city distances
dist_matrix = [[distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]