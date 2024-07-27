import itertools
import math
from scipy.spatial.distance import pdist, squareform
from sympy.utilities.iterables import multiset_permutations

def calculate_distance(coords1, coords2):
    return math.sqrt((coords2[0] - coords1[0])**2 + (coords2[1] - coords1[1])**2)

# City coordinates including the depot
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate pairwise distances
distances = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Base case: find tour including depot and any combination of 15 more cities
min_route_cost = float('inf')
optimal_route = []

# Check all possible combinations of 15 other cities (since total should be 16 including depot)
for combination in itertools.combinations(range(1, 20), 15):
    full_combination = [0] + list(combination) + [0]  # start and end at the depot
    for permutation in multiset_permutations(full_combination[1:-1]):  # All permutations of the middle part
        candidate_route = [0] + list(permutation) + [0]
        current_cost = sum(distances[candidate_route[i]][candidate_route[i+1]] for i in range(len(candidate_route) - 1))
        
        if current_cost < min_route_cost:
            min_route_cost = current_cost
            optimal_route = candidate_street

print(f"Tour: {optimal_route}")
print(f"Total travel cost: {min_route_cost}")