import math
import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Define city coordinates
cities = {
    0: (16, 90), 
    1: (43, 99), 
    2: (80, 21),
    3: (86, 92), 
    4: (54, 93), 
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Calculate distance matrix using Euclidean distance
def calculate_distance_matrix(cities):
    coords = np.array(list(cities.values()))
    return distance_matrix(coords, coords)

dist_matrix = calculate_distance_matrix(cities)

# A simple nearest neighbor algorithm as a quick attempt to minimize the max distance in the tour
def nearest_neighbor_tour(start, dist_matrix):
    n = len(dist_matrix)
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unaccepted, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # return to the starting city
    return tour

# Function to calculate total distance and maximum leg distance in a tour
def evaluate_tour(tour, dist_matrix):
    total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_leg_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost, max_leg_distance

# Generate tour and calculate cost metrics
tour = nearest_neighbor_tour(0, dist_matrix)
total_cost, max_leg_distance = evaluate_tour(tour, dist_matrix)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_leg_distance}")