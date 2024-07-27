import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Euclidean distance calculation
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generating the full distance matrix
def calculate_distances(cities):
    num_cities = len(cities)
    distance_matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])
    return distance_matrix

# Creating a tour from the MST
def create_mst_tour(cities):
    distances = calculate_distances(cities)
    distance_matrix = csr_matrix(distances)
    mst = minimum_spanning_tree(distance_matrix).toarray()
    
    # Creating a simple tour from MST by DFS
    visited = set()
    tour = []
    
    def dfs(current):
        visited.add(current)
        tour.append(current)
        for next_city in range(len(cities)):
            if mst[current][next_city] != 0 and next_city not in visited:
                dfs(next_city)
    
    dfs(0)  # Start DFS from node 0 (depot)
    tour.append(0)  # conclude tour by returning to the depot
    return tour, distances

# Evaluate tour metrics: Total Distance and Maximum Single Step Distance
def evaluate_tour(tour, distances):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        step_distance = distances[tour[i]][tour[i + 1]]
        total_distance += step_distance
        if step_distance > max_distance:
            max_distance = step_distance
    return total_distance, max_distance

# Define cities by coordinates
cities = [
    (54, 87),  # Depot
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Resolve the problem
tour, distances = create_mst_tour(cities)
total_cost, max_distance = evaluate_tour(tour, distances)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")