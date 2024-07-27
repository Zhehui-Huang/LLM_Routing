import math
from itertools import product

# Define the city coordinates
city_coords = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), 
    (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), 
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Define city groups
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Pre-compute all pairwise distances
distances = {}
for i in range(len(city_coords)):
    for j in range(len(city_coords)):
        if i not in distances:
            distances[i] = {}
        distances[i][j] = euclidean_distance(city_coords[i], city_coords[j])

# Helper function to compute the total cost of the tour
def tour_cost(tour):
    total_cost = 0
    for k in range(len(tour) - 1):
        total_cost += distances[tour[k]][tour[k + 1]]
    total_cost += distances[tour[-1]][tour[0]]  # Return to depot
    return total_cost

# Brute-force search over all combinations
min_cost = float('inf')
best_tour = None

# All possible selections, one city from each group and every permutation
for selection in product(*city_groups):
    for permuted_selection in permutations(selection):
        current_tour = [0] + list(permuted_selection) + [0]
        current_cost = tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")