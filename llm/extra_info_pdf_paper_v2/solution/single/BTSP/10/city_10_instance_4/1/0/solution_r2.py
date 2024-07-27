import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order

# Define the coordinates of the cities
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Construct a NumPy array of coordinates
coords = np.array(list(cities.values()))

# Compute the Euclidean distance matrix
dist_matrix = distance_matrix(coords, coords)

# Minimum spanning tree (MST) of the graph based on the distance matrix
mst = minimum_spanning_tree(dist_matrix)
mst = mst.toarray().astype(float) + mst.T.toarray().astype(float)  # Making the MST symmetrical

# Perform a depth-first search (DFS) on this MST to obtain a preliminary tour
_, prelim_tour = depth_first_order(mst, directed=False, i_start=0, return_predecessors=False)

# Ensuring the tour starts and ends at the depot (city 0)
tour_candidate = list(dict.fromkeys(prelim_tour))  # Removing duplicates while preserving order
if tour_candidate[-1] != 0:
    tour_candidate.append(0)

# Identifying maximum distance and total travel distance in this tour
max_distance = 0
total_travel_cost = 0

for i in range(1, len(tour_candidate)):
    city_a = tour_candidate[i - 1]
    city_b = tour_candidate[i]
    dist = dist_matrix[city_a, city_b]
    total_travel_cost += dist
    if dist > max_distance:
        max_distance = dist

# Display the outcomes
print(f"Tour: {tour_candidate}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")