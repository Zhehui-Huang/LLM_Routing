import numpy as np
import itertools

# Coordinates of the cities including the depot
locations = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(loc1, loc2):
    """ Compute Euclidean distance between two points. """
    return np.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

def calculate_total_and_max_dist(tour, distance_matrix):
    """ Calculate total travel cost and maximum distance between consecutive cities in a tour. """
    total_cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    max_dist = max(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost, max_dist

# Precompute the distance matrix
n = len(locations)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = euclidean_delta(locations[i], locations[j])

# Trying permutations to find an optimal tour minimizing the maximum distance between consecutive cities
min_max_dist = float('inf')
best_tour = None

for perm in itertools.permutations(range(1, n)):  # Iterate over permutations of cities excluding the depot
    tour = [0] + list(perm) + [0]  # Start and end at the depot
    _, max_dist = calculate_total_and_max_dist(tour, dist_matrix)
    
    if max_dist < min_max_dist:
        min_max_dist = max_dist
        best_tour = tour

# Output the results for the best found tour
if best_tour:
    total_cost, max_distance = calculate_total_and_max_dist(best_tour, dist_matrix)
    print("Tour:", best_tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)