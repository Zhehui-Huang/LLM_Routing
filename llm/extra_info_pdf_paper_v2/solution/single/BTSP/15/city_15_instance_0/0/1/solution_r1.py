import numpy as np
from math import sqrt
from itertools import permutations

# City coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23),
    (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Calculate the Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Creating a distance matrix
def calculate_distance_matrix(cities):
    number_of_cities = len(cities)
    distance_matrix = [[0] * number_of_cities for _ in range(number_of_cities)]
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                distance_matrix[i][j] = float('inf')
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

# Find tour minimizing maximum edge length (brute force for exact solution)
def find_optimal_tour(distance_matrix):
    n = len(distance_matrix)
    best_tour = None
    min_max_distance = float('inf')
    all_tours = permutations(range(1, n))  # all possible tours excluding the depot which is city 0
    
    for perm in all_tours:
        tour = [0] + list(perm) + [0]
        max_distance_in_tour = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_distance_in_tour < min_max_distance:
            min_max_distance = max_distance_in_tour
            best_tour = tour
            
    return best_tour, min_max_distance

best_tour, max_edge_length = find_optural_tour(distance_matrix)

# Calculate total distance
def total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

total_travel_cost = total_distance(best_tour, distance_matrix)

# Output results
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_edge_length)