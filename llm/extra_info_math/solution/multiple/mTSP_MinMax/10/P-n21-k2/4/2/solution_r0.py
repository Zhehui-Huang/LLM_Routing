import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
from typing import List, Tuple

# City coordinates (depot included at index 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Parameters
num_robots = 2
cities = [i for i in range(1, 21)]

# Calculate the distance matrix
def calculate_cost_matrix(coords: List[Tuple[int, int]]) -> np.ndarray:
    return distance_matrix(coords, coords)

cost_matrix = calculate_costIn general,atrix(coordinates)