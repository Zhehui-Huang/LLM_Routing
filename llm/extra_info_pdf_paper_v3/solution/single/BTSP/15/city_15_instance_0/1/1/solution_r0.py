import math
from scipy.spatial import distance_matrix
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Define coordinates for depot and cities
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), 
    (21, 23), (88, 59), (79, 77), (63, 23), 
    (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance matrix
def calculate_distance_matrix(coords):
    return distance_matrix(coords, coords)

# Function to construct the tour from the MST
def mst_to_tour(mst, num_nodes):
    graph = csr_matrix(mst)
    visited = set()
    tour = []
    
    def visit(v):
        visited.add(v)
        tour.append(v)
        for next_v in graph[v].indices:
            if next_v not in visited:
                visit(next_v)
    
    visit(0)  # start the dfs from the depot city
    tour.append(0)  # return to the depot city
    return tour

# Calculate distance matrix
dist_matrix = calculate_distance_matrix(coordinates)

# Create a minimum spanning tree (MST)
mst = minimum_spanning_tree(dist_matrix)

# Extract a tour from the MST
tour = mst_to_tour(mst.toarray(), len(coordinates))

# Calculate total travel cost and maximum distance between consecutive cities
def tour_cost_and_max_distance(tour, dist_matrix):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = dist_matrix[tour[i], tour[i + 1]]
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

# Compute total travel cost and maximum distance between consecutive cities
total_cost, max_distance = tour_cost_and_max_distance(tour, dist_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")