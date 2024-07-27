import numpy as np
from scipy.spatial import distance_matrix
from itertools import product
from ortools.linear_solver import pywraplp

# Define cities coordinates
cities_coord = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Compute the distance matrix
distances = distance_matrix(cities_coord, cities_coord)

# Number of robots and cities including the depot
num_robots = 4
num_cities = len(cities_coord)