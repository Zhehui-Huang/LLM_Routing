import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations, permutations

# Coordinates of the cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Function to calculate distance matrix
def distance_matrix(coords):
    num_cities = len(coords)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            dist = euclidean(coords[i], coords[j])
            matrix[i, j] = matrix[j, i] = dist
    return matrix

# Number of cities to visit including the depot (10)
k = 10

# Generate the distance matrix
dist_matrix = distance_matrix(coordinates)

# Generate all possible combinations to select 9 other cities (excluding city 0)
comb = combinations(range(1, 15), k-1)

# For finding the best short tour
min_cost = float('inf')
best_tour = None

# Check combinations including the depot
for cities in comb:
    # Include city 0 in each combination
    tour_cities = [0] + list(cities)
    
    # Generate all permutations of the selected cities for minimum tour calculation
    for perm in permutations(tour_cities):
        # Check if the cycle starts and ends at the depot (city 0)
        if perm[0] == 0 and perm[-1] == 0:
            cost = sum(dist_matrix[perm[i], perm[i+1]] for i in range(len(perm) - 1))
            
            if cost < min_cost:
                min_cost = cost
                best_tour = perm

# Display results
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {min_cost:.2f}")