import numpy as np
from itertools import permutations

# Given cities and coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 7),
    9: (6, 76)
}

# Function to calculate Euclidean distance
def calculate_distance(c1, c2):
    return np.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Number of cities
num_cities = len(cities)

# Calculating all distances matrix
distances = [[calculate_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Brute-force method to find the optimal path minimizing the maximum edge length
def find_min_max_tour():
    min_max_distance = float('inf')
    optimal_tour = None
    
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_distance_in_tour = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_distance_in_tour < min_max_distance or (max_distance_in_tour == min_max_distance and total_distance < sum(distances[optimal_tour[i]][optimal_tour[i+1]] for i in range(len(optimal_tour) - 1))):
            min_max_distance = max_distance_in_tour
            optimal_tour = tour
    
    return optimal_tour, min_max_distance

# Solve the problem
optimal_tour, min_max_distance = find_min_max_tour()
total_travel_cost = sum(distances[optimal_tour[i]][optimal_tour[i+1]] for i in range(len(optimal_tour) - 1))

# Output results
print("Tour:", optimal_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", min_max_distance)