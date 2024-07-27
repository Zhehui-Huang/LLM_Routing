import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Define city coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# k cities to visit including the depot
k = 10

# Function to calculate the Euclidean distance matrix
def calculate_distance_matrix(cities):
    return distance_matrix(cities, cities)

# Function to calculate total travel cost of a tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Get distance matrix
dist_matrix = calculate_distance_matrix(cities)

# Hyper-Heuristic function to find a short tour
def find_shortest_k_tsp_tour(dist_matrix, num_cities, k):
    best_tour = None
    best_cost = float('inf')
    city_indices = list(range(num_cities))
    for subset in permutations(city_indices[1:], k-1):  # exclude depot city 0 initially, then add later
        current_subset = [0] + list(subset) + [0]  # add depot city to start and end
        cost = calculate_tour_cost(current_subset, dist_matrix)
        if cost < best_cost:
            best_cost = cost
            best_tour = current_subset
    return best_tour, best_cost

# Get the best tour
best_tour, best_cost = find_shortest_k_tsp_tour(dist_matrix, len(cities), k)

# Print the solution
print("Tour:", best_tour)
print("Total travel cost:", best_cost)