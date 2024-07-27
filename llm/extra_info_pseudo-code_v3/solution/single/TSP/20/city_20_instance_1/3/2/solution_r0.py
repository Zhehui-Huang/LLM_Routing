import math
from scipy.spatial import distance_matrix
import numpy as np
from networkx import Graph, minimum_spanning_tree, eulerian_circuit, set_node_attributes
from networkx.algorithms.matching import min_weight_matching
from itertools import combinations

# Cities coordinates (city index starts from 0)
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Distance matrix calculation
dist_matrix = distance_matrix(cities, cities)

# Total number of cities
num_cities = len(cities)