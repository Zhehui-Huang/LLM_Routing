import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_bottleneck_tour(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    
    # Calculate all pairwise distances
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean_point_distance(cities[i], cities[j])
    
    # Permutation based approach to find tour with minimum maximum distance between consecutive cities
    min_max_distance = float('inf')
    best_tour = []
    
    # Check all possible permutations, skipping permutations that do not start with the depot city to optmize
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_distance_in_tour = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_distance_in_tour < min_max_distance:
            min_max_distance = max_distance_in_tour
            best_tour = tour
    
    # Calculate total travel cost for the best tour found
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
    
    return best_tour, total_cost, min_max_distance

# Define cities
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), (90, 85),
          (98, 76), (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Get the optimal tour
tour, total_cost, max_distance = find_bottleneck_tour(cities)

# Print outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")