import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms.approximation import christofides_tsp
from itertools import combinations
import matplotlib.pyplot as plt

# City coordinates
cities_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate distance matrix
dist_matrix = distance_matrix(cities_coordinates, cities_coordinates)