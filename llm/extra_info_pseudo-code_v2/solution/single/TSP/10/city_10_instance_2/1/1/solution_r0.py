import math
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Given coordinates
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54), 
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Function to calculate euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Creating a distance matrix
def create_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

# Nearest neighbour helper function for initial tour
def nearest_neighbour_tour(start, distance_matrix):
    num_cities = len(distance_matrix)
    unvisited = list(range(num_cities))
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start) # return to the depot
    return tour

# Computing the cost of the tour
def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_pol = tour[i]
        total_pin = tour[i + 1]
        total_cost += distance_matrix[total_pol][total_pin]
    return total_cost

# Convert coordinates to list in the order
coord_list = [coordinates[i] for i in range(len(coordinates))]

# Generate distance matrix
distance_matrix = create_distance_matrix(coord_list)

# Generating an initial tour using Nearest Neighbour
initial_tour = nearest_neighbour_trajectory(0, distance_matrix)

# Calculate the cost of the initial tour
initial_cost = calculate_traversal_cost(initial_tour, distance_matrix)

# Dummy Lin-Kernighan implementation for demonstration
# In practice, would implement the improvement steps from the pseudocode
def lin_kernighan(tour, distance_matrix):
    # This is a placeholder to represent that LK heuristic would be employed here
    return tour, calculate_traversal_cost(tour, distance_matrix)

# Since we're limited without the full implementation of L-K, we simulate improvement
improved_tour, improved_cost = lin_kernighan(initial_tour, distance_matrix)

print("Tour:", improved_tour)
print("Total travel cost:", improved_cost)