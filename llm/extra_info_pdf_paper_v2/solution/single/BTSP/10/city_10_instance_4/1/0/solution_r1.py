import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order

# Define the coordinates of the cities
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Calculate the Euclidean distance matrix
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Create the MST
mst = minimum_spanning_tree(dist_matrix)
mst = mst.toarray().astype(float) + mst.T.toarray().astype(float)  # Symmetric MST needed for undirected graph

# Use DFS to create a tour from the MST
_, dfs_order = depth_first_order(mst, directed=False, i_start=0, return_predecessors=False)
tour = list(dict.fromkeys(dfs_order))  # This removes duplicates but keeps order

# Ensure the tour starts and ends at the depot city
if tour[-1] != 0:
    tour.append(0)

# Calculate maximum consecutive distance and total travel cost
max_distance = 0
total_travel_cost = 0

for i in range(len(tour) - 1):
    city_a = tour[i]
    city_b = tour[i + 1]
    dist = dist_matrix[city_a, city_b]
    total_travel_cost += dist
    if dist > max_distance:
        max_distance = dist

# Outputting the results
print(f"Tour: {tour}")
print(f"Total travel cost: {int(total_travel_cost)}")
print(f"Maximum distance between consecutive cities: {int(max_distance)}")