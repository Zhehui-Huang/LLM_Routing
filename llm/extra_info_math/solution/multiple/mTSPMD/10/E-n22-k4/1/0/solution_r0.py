import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates
coordinates = [
    (145, 215), # Depot 0
    (151, 264), # Depot 1
    (159, 261), # Depot 2
    (130, 254), # Depot 3
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of nodes and depots
num_nodes = len(coordinates)
num_depots = 4
num_robots = num_depots

# Distance matrix
def euclidean_distance(coord1, coord2):
    return np.linalg.norm(np.subtract(coord1, coord2))

distance_matrix = np.array(
    [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_nodes)]
     for i in range(num_nodes)]
)

# Depot index for all robots
depot_indices = [0, 1, 2, 3]