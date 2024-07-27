import numpy as  np
from itertools import permutations

# City Coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(p1, p2):
    """Calculate euclidean distance between two points."""
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the distance matrix
n = len(coordinates)
dist_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_differentiation(coordinates[i], coordinates[j])
        dist_matrix[i][j] = dist
        dist_matrix[j][i] = dist

# Brute-force approach to find minimal bottleneck distance tour (only feasible for small n)
def find_min_bottleneck_tour():
    best_tour = None
    min_bottleneck = float('inf')
    
    # Check all permutations of cities (without starting city 0)
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_dist = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        
        if max_dist < min_bottleneck:
            min_bottleneck = max_dist
            best_tour = tour
    
    # Calculate the total cost of the optimal tour
    total_cost = sum(dist_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    
    return best_tour, total_cost, min_bottleneck

# Execute the function and print the output
best_tour, total_cost, max_distance = find_min_bottleneck_tour()
output = {
    'Tour': best_tour,
    'Total travel cost': total_cost,
    'Maximum distance between consecutive cities': max_distance
}
print(output)