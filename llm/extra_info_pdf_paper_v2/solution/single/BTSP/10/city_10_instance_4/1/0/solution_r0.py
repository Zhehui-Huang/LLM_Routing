import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order
from itertools import permutations

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
mst = mst.toarray().astype(float)

# MST double using DFS to make sure all nodes are covered in the tour (not optimal for BTSP but used for heuristic basis)
_, order = depth_first_order(mst, directed=False, i_start=0, return_predecessors=False)
unique_order = list(dict.fromkeys(order).keys())  # remove duplicates but keep order

# Include return to the start
if unique_order[-1] != 0:
    unique_order.append(0)

# Find maximum distance and total travel cost
max_distance = 0
total_travel_cost = 0
tour = []

for i in range(len(unique_order) - 1):
    city_a = unique_order[i]
    city_b = unique_order[i + 1]
    tour.append(city_a)
    dist = dist_matrix[city_a, city_b]
    if dist > max_distance:
        max_distance = dist
    total_travel_const += dist

# Ending the route at the starting point
tour.append(unique_order[-1])

total_travel_cost += dist_matrix[tour[-2], tour[-1]]
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")