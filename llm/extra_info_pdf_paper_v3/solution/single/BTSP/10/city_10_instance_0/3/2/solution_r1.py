import math
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

# Define city coordinates
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), 
          (62, 26), (79, 31), (61, 90), (42, 49)]

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

# Find Euler tour from the MST
def euler_tour_from_mst(graph, start=0):
    visited = [False] * len(graph)
    tour = []
    find_pre_order(start, -1, graph, visited, tour)
    tour.append(start)  # Complete the cycle
    return tour

# Getting Euler tour from MST
tour_approx = euler_tour_from_mst(mst)

# Helper function to refine Euler tour to a valid TSP tour
def refine_tour(euler_tour):
    visited = set()
    refined_tour = []
    for city in euler_tour:
        if city not in visited:
            visited.add(city)
            refined_tour.append(city)
    if refined_tour[0] != refined_tour[-1]:  # Ensure it's a cycle
        refined_tour.append(refined_tour[0])
    return refined_tour

# Refine the tour to meet TSP constraints
tsp_tour = refine_tour(tour_approx)

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
print("Tour:", tsp_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)