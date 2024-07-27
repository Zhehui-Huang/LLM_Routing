import math
from scipy.spatial import distance_matrix
import numpy as np

# City Coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Compute Euclidean distances between cities
coords = np.array([cities[i] for i in range(len(cities))])
dist_matrix = distance_matrix(coords, coords)

def create_tour():
    from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order

    # Using Minimum Spanning Tree to approximate a bottleneck-optimal subgraph
    mst = minimum_spanning_tree(dist_matrix)
    # Get the MST in array form (needed for traversing)
    mst_array = mst.toarray().astype(float)
    
    # Perform a DFS to get a tour from the MST, starting from the depot city 0
    tree_order = depth_first_order(mst, 0, directed=False)[0]
    
    # Since it's a tree-based DFS, we need to make sure to return to start.
    tour = list(tree_order) + [0]
    
    # Calculate total travel cost and max distance between consecutive cities
    max_distance = 0
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        src = tour[i]
        dst = tour[i+1]
        travel_cost = dist_matrix[src][dst]
        total_travel_cost += travel_cost
        if travel_cost > max_distance:
            max_distance = travel_cost
    
    return tour, total_travel_cost, max_distance

# Generate and output the tour, total cost, and maximum distance.
tour, total_cost, max_distance = create_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")