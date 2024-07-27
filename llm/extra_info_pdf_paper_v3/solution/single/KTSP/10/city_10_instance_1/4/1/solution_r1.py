import math
from itertools import permutations, combinations

# Coordinates of the cities (depot is index 0)
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), 
               (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute distance matrix
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Evaluate cost of a given tour
def evaluate_tour(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Finding the best tour among 5-city tours including the depot
min_cost = float('inf')
best_tour = None

# We search through all combinations of 4 cities excluding the depot (indices 1-9)
for cities in combinations(range(1, 10), 4):
    current_subset = [0] + list(cities) + [0]  # Include depot as start and end
    # Find all permutations of the inner cities
    for perm in permutations(current_subset[1:-1]):
        candidate_tour = [0] + list(perm) + [0]
        cost = evaluate_tour(candidate_tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = candidate_tour

# Output the tour
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))