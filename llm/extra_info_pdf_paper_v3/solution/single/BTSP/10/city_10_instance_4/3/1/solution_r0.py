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
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest neighbor heuristic to obtain an initial tour
def nearest_neighbor_tour(start=0):
    unvisited = set(range(n))
    current = start
    tour = [current]
    unvisited.remove(current)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
        
    tour.append(start)  # Return to start
    return tour

# Calculate tour details
def calculate_tour_details(tour):
    total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost, max_sale

# Generate tour
tour = nearest_neighbor_tour()
total_cost, max_distance = calculate_tour_details(tour)

# Output must include the tour, total travel cost, and max distance
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")