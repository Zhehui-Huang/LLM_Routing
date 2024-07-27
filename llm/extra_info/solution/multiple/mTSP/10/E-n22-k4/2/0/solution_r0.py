import math
import numpy as np
from scipy.spatial.distance import pdist, squareform

# Define city coordinates
coordinates = [
    (145, 215), # Depot city 0
    (151, 264), # City 1
    (159, 261), # City 2
    (130, 254), # City 3
    (128, 252), # City 4
    (163, 247), # City 5
    (146, 246), # City 6
    (161, 242), # City 7
    (142, 239), # City 8
    (163, 236), # City 9
    (148, 232), # City 10
    (128, 231), # City 11
    (156, 217), # City 12
    (129, 214), # City 13
    (146, 208), # City 14
    (164, 208), # City 15
    (141, 206), # City 16
    (147, 193), # City 17
    (164, 193), # City 18
    (129, 189), # City 19
    (155, 185), # City 20
    (139, 182)  # City 21
]

# Calculate distance matrix using Euclidean distance
def distance_matrix(coords):
    matrix = squareform(pdist(coords, metric='euclidean'))
    return matrix

dist_matrix = distance_matrix(coordinates)

# Number of Robots
num_robots = 4