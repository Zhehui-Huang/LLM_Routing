import math
from itertools import permutations

# Given data
positions = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Helper function to calculate Euclidean distance
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generating all pairwise distances for convenience
distances = {(i, j): dist(positions[i], positions[j]) for i in positions for j in positions if i != j}

# Function to determine the bottleneck distance in a given tour
def calculate_bottleneck(tour):
    bottleneck = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    return total_cost, bottleneck

# Generate possible tours
cities = list(positions.keys())
min_bottleneck_value = float('inf')
best_tour = None

for perm in permutations(cities[1:]):  # exclude the depot from permutations
    tour = [0] + list(perm) + [0]
    total_cost, bottleneck = calculate_bottleneck(tour)
    if bottleneck < min_bottleneck_value:
        min_bottleneck_value = bottleneck
        best_tour = tour
        best_cost = total_cost

# Output results based on the heuristic BTSP problem solving strategy
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")
print(f"Maximum distance between consecutive cities: {min_bottleneck_value}")