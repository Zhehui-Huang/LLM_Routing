import math
import itertools

# Defining cities with their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Group of cities
groups = [
    [7, 9],  # Group 0
    [1, 3],  # Group 1
    [4, 6],  # Group 2
    [8],     # Group 3
    [5],     # Group 4
    [2]      # Group 5
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Precompute distances between every pair of cities
distances = {
    (i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities
}

def find_optimal_tour():
    min_cost = float('inf')
    best_tour = None

    # Generate every combination of selecting one city from each group
    for selection in itertools.product(*groups):
        all_permutations = itertools.permutations(selection)
        for perm in all_permutations:
            tour = [0] + list(perm) + [0]
            cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    return best_tour, min_cost

# Find the optimal tour
optimal_tour, optimal_cost = find_optimal_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")