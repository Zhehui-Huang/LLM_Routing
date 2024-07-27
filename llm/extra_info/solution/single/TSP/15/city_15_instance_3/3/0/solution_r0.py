from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import shortest_path
from scipy.optimize import linear_sum_assignment
import numpy as np

# Defining the cities' coordinates
coordinates = np.array([
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
])

# Calculate the Euclidean distances
dist_matrix = squareform(pdist(coordinates, metric='euclidean'))

# For TSP, we need to interpret the dist_matrix as an adjacency matrix-based input
from scipy.sparse.csgraph import tsp

# The TSP method needs a precomputed distance matrix
tour_cost, tour = tsp(dist_matrix)

# We need to ensure the tour starts and ends at the depot city, index 0
# Since the solver might give a tour starting from any city,
# we need to rotate the city list to start from 0.
def find_and_rotate_tour(tour, start):
    start_index = np.where(tour == start)[0][0]
    return np.roll(tour, -start_index)

# Adjust the tour
adjusted_tour = find_and_rotate_tour(tour, 0)

# Including return to the depot city at the end of the tour
full_tour = np.append(adjusted_tour, adjusted_tour[0])

print(f"Tour: {full_tour.tolist()}")
print(f"Total travel cost: {tour_cost}")