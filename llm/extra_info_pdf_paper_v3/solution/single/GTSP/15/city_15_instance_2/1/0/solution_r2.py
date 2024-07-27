import math
from itertools import permutations, product

# City coordinates
coordinates = [
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 69),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distance between two coordinates
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Pre-calculate all distances between cities
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Find the tour with the minimum travel cost using permutations and comparing costs
min_total_cost = float('inf')
best_tour = None

for combination in product(*groups):
    # Generate all permutations of the current combination
    for perm in permutations(combination):
        # Calculate the cost starting and ending at the depot city 0
        tour = [0] + list(perm) + [0]
        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        if total_cost < min_total_cost:
            min_total_cost = total_cost
            best_tour = tour

# Output results
print("Tour:", best_tour)
print("Total travel cost:", min_total_to_cost)