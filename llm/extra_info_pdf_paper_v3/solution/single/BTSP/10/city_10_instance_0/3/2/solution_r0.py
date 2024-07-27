import math
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from itertools import permutations

# Define city coordinates
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Calculate Euclidean distance matrix
dist_matrix = distance_matrix(cities, cities)

# Calculate a Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix).toarray()

# Helper function to find pre order of TSP tour from MST
def find_pre_order(node, parent, graph, visited, tour):
    visited[node] = True
    tour.append(node)
    for i in range(len(graph)):
        if graph[node][i] != 0 and not visited[i]:
            find_pre_order(i, node, graph, visited, tour)

# Find Euler tour of the MST (MST must be used to generate a full tour)
def euler_tour_from_mst():
    visited = [False] * len(cities)
    tour = []
    find_pre_order(0, -1, mst, visited, tour)
    return tour

# Getting Euler tour from MST
tour_approx = euler_tour_from_mst()

# Convert Euler tour to a valid TSP tour
tsp_tour = []
visited = set()
for city in tour_approx:
    if city not in visited:
        visited.add(city)
        tsp_tour.append(city)
tsp_tour.append(tsp_tour[0])  # to make it a cycle

# Calculate total cost and maximal distance in the tour
def calculate_tour_costs(tour, dist_matrix):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = dist_matrix[tour[i]][tour[i+1]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

total_cost, max_distance = calculate_tour_costs(tsp_tour, dist_matrix)

# Output the tour, total cost, and maximum distance
output = {
    "Tour": tsp_tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}
output