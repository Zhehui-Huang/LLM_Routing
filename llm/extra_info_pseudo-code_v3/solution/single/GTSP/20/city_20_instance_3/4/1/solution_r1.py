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

def euclidean_distance(index1, index2):
    return math.sqrt((coordinates[index1][0] - coordinates[index2][0]) ** 2 + (coordinates[index1][1] - coordinates[index2][1]) ** 2)

# Generate all combinations: one city from each group
all_combinations = itertools.product(*groups)

best_tour = None
best_tour_cost = float('inf')

# Try every combination of cities (one from each group)
for combination in all_combinations:
    # Permutations of the chosen cities in the combination
    for perm in itertools.permutations(combination):
        # Calculate the cost of the tour for this permutation
        total_cost = euclidean_distance(0, perm[0])  # Depot to first city
        for i in range(len(perm) - 1):
            total_cost += euclidean_distance(perm[i], perm[i + 1])
        total_cost += euclidean_distance(perm[-1], 0)  # Last city back to depot
        
        # Check if this permutation is better (i.e. costs less)
        if total_cost < best_tour_cost:
            best_tour_cost = total_cost
            best_tour = [0] + list(perm) + [0]

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)