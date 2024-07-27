import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Coordinates of each city including the depot (indexed from 0 to 9)
coordinates = np.array([
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69), 
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
])

# Calculate the euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

def find_tour_bottleneck(distances):
    # All cities excluding the depot for permutation purposes
    cities = list(range(1, len(distances)))
    
    # Variable to store the minimum maximum edge cost found
    min_max_distance = float('inf')
    best_tour = None
    
    # Generate all permutations of cities and calculate corresponding metrics
    for perm in permutations(cities):
        tour = [0] + list(perm) + [0]  # start and end at the depot
        max_dist_in_tour = max(
            distances[tour[i], tour[i+1]] for i in range(len(tour) - 1)
        )
        
        if max_dist_in_tour < min_max_distance:
            min_max_meet_distance = max_dist_in_tour
            best_tour = tour

    # Calculate the total cost of the best tour found
    total_distance = sum(distances[best_tour[i], best_tour[i+1]] for i in range(len(best_tour) - 1))
    
    return best_tour, total_distance, min_max_distance

# Find the tour minimizing the maximum distance between consecutive cities
tour, total_travel_cost, max_distance_between_cities = find_tour_bottleneck(dist_matrix)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_between_cities)