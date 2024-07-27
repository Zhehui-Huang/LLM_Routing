import numpy as np
import math

# City coordinates
coordinates = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61),
    (22, 21), (97, 70), (20, 99), (66, 62)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point0[1] - point1[1])**2)

# Create a distance matrix
n = len(coordinates)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest Neighbor approach for an initial heuristic tour
def nearest_neighbor_tour(start=0):
    visited = set()
    visited.add(start)
    tour = [start]
    current = start
    
    while len(visited) < n:
        next_city = min((i for i in range(n) if i not in visited), key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        visited.add(next_city)
        current = next_city
    
    tour.append(start)  # return to depot
    return tour

# Generating the tour using the Nearest Neighbor heuristic
tour = nearest_neighbor_tour()

# Calculating total travel cost and max distance between any two consecutive cities
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")