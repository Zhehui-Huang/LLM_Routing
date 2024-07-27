import pulp as lp
import math

# Define the city coordinates, excluding the depot which is indexed at 0
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Calculate the Euclidean distance between two cities
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Number of cities (including depot)
n = len(coordinates)

# Define the cost matrix
cost = [[calc_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Number of salesmen (robots)
m = 4