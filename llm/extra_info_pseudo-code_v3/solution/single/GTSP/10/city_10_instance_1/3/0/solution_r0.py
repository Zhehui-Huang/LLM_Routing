import math
from itertools import product

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Definition of cities and their coordinates
cities = {
    0: (53, 68),  # Depot
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

# List of groups as per the problem requirement
groups = [[5, 6, 7], [2, 3], [1, 9], [4, 8]]

# Compute the problem as an all pairs distance matrix using Euclidean distances
distances = {}
for c1, c2 in product(cities.keys(), repeat=2):
    if c1 not in distances:
        distances[c1] = {}
    distances[c1][c2] = euclidean_distance(cities[c1], cities[c2])

# We need to find one city from each group and calculate the optimal path
from itertools import permutations

# Initialize optimal tour information
min_cost = float('inf')
optimal_tour = []

# Generate all permutations of one representative from each group
group_permutations = list(product(*groups))
for group_perm in group_permutations:
    # Try all permutations of chosen representatives
    for perm in permutations(group_perm):
        # Start at the depot, go through the selected cities, and back to the depot
        tour = [0] + list(perm) + [0]
        current_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        if current_cost < min_cost:
            min_cost = current_cost
            optimal_tour = tour

# Output the shortest tour and the corresponding total travel cost
print("Tour:", optimal_tour)
print("Total travel cost:", round(min_cost, 2))