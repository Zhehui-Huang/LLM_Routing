import numpy as np
from itertools import permutations

# City Coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the distance matrix
n = len(coordinates)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        dist_matrix[i][j] = dist
        dist_matrix[j][i] = dist

# Function to search for a tour with the minimal maximal distance between consecutive cities.
def find_min_max_distance_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Iterating over all permutations excluding the depot (index 0)
    for perm in permutations(range(1, n)):
        # Considering the depot in the tour
        current_tour = [0] + list(perm) + [0]
        
        # Finding the maximum and total distances in the current tour permutation
        max_distance = max(dist_matrix[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
        total_cost = sum(dist_matrix[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
        
        # Updating the best tour found
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
            best_max_distance = max_distance
            best_total_cost = total_cost
            best_tour = current_tour

    return best_tour, best_total_cost, best_max_distance

# Running the function and obtaining the results
tour, total_cost, max_distance = find_min_max_distance_tour()
output = {
    'Tour': tour,
    'Total travel cost': total_cost,
    'Maximum distance between consecutive cities': max_distance
}

print(output)