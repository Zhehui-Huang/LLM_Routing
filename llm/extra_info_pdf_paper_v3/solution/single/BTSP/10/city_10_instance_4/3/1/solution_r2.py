import numpy as np
import math

# City coordinates
coordinates = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61),
    (22, 21), (97, 70), (20, 99), (66, 62)
]

# Number of cities
n = len(coordinates)

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create a distance matrix
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Find the nearest neighbor tour starting from the depot (city 0)
def nearest_neighbor(start=0):
    visited = [False] * n
    visited[start] = True
    tour = [start]
    current = start

    for _ in range(1, n):
        next_city = min(
            [(j, distance_matrix[current][j]) for j in range(n) if not visited[j]],
            key=lambda x: x[1])
        current = next_city[0]
        tour.append(current)
        visited[current] = True

    tour.append(start)  # Return to the starting point (depot)
    return tour

# Generate tour
tour = nearest_neighbor()

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output must include the tour, total travel cost, and max distance
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")