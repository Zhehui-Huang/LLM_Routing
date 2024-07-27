import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Number of cities to visit including the depot
k = 12  

# Compute distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean(cities[i], cities[j])

# Calculate all (k-1) subsets of the cities excluding the depot, since depot is included
all_possible_cities = list(range(1, n))
subsets = list(combinations(all_possible_cities, k - 1))

# Function to compute the cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i], tour[i+1]]
    return cost

# Find the optimal tour
min_cost = float('inf')
best_tour = None

for subset in subsets:
    current_cities = [0] + list(subset)
    # Calculate all permutations for the selected cities including a return to the depot
    for perm in permutations(current_cities):
        complete_tour = list(perm) + [0]
        cost = calculate_tour_cost(complete_tour, distance—I'm)
        if cost < min_cost:
            min_cost = cost
            best_tour = complete_tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", min_cost)