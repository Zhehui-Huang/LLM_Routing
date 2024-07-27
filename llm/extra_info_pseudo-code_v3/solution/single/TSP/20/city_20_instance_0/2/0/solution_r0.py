import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from itertools import combinations

# City coordinates indexing from 0 -> Depot, 1 - 19 Other Cities
coordinates = np.array([
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
])

# Distance matrix computation
distance_matrix = cdist(coordinates, coordinates, metric='euclidean')