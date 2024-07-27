import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order

# Define the cities positions
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Compute the distance matrix
dist_matrix = distance_matrix(cities, cities)

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to find MST and then create a tour from it
def minimum_spanning_tree_tour():
    mst = minimum_spanning_tree(dist_matrix).toarray()
    tour = depth_first_order(mst, 0, directed=False)[0]
    return np.append(tour, tour[0])  # to make it a cycle

# Function to calculate tour cost and maximum edge cost
def tour_cost(tour):
    total_cost = 0
    max_edge_cost = 0
    for i in range(len(tour) - 1):
        edge_cost = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += edge_cost
        max_edge_cost = max(max_edge_cost, edge_cost)
    return total_cost, max_edge_cost

# Compute the tour
tour = minimum_spanning_tree_tour()
total_cost, max_edge_cost = tour_cost(tour)

# Output results
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge_cost:.2f}")