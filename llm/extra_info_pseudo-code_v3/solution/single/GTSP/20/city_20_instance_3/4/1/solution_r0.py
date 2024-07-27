import itertools
import math

# Coordinates of the cities
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix computation
dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

def find_min_cost_permutation(perm):
    # Start at the depot, visit each in perm, return to depot
    cost = dist_matrix[0][perm[0]] + dist_array[perm[-1]][0]
    for i in range(len(perm) - 1):
        cost += dist_matrix[perm[i]][perm[i+1]]
    return cost

# Generate all candidate city sets, one from each group
all_candidate_sets = [list(itertools.product([0], group)) for group in groups]
all_candidate_combinations = list(itertools.product(*all_candidate_sets))

best_tour_cost = float('inf')
best_tour = None

# Brute force over all combinations
for candidate in all_candidate_combinations:
    # Flatten the candidate list and ensure uniqueness except the depot (0)
    candidate_cities = [item for sublist in candidate for item in sublist if item != 0]
    # Compute the best tour permutation among selected cities
    perms = itertools.permutations(candidate_cities)
    for perm in perms:
        cost = find_min_cost_permutation((0, ) + perm + (0,))
        if cost < best_tour_cost:
            best_tour_cost = cost
            best_tour = (0, ) + perm + (0,)

# Output the results
print("Tour:", list(best_tour))
print("Total travel cost:", best_tour_cost)