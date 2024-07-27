import numpy as  np
import sys

# Define the cities' coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

n = len(coordinates)

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return round(np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2), 2)

# Create the distance matrix
dist_matrix = np.full((n, n), float('inf'))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Function to perform the nearest neighbor method as an insertion heuristic
def nearest_neighbor_tour(start):
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start)
    return tour

# Function to calculate the cost of the tour
def tour_cost(tour, dist_matrix):
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost

# Function to find maximum distance between consecutive cities in the tour
def max_distance_in_tour(tour, dist_matrix):
    max_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return max_distance

# Generate the tour
tour = nearest_neighbor_tour(0)
total_cost = tour_cost(tour, dist_matrix)
max_distance = max_distance_in_tour(tour, dist_matrix)

# Results display
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)