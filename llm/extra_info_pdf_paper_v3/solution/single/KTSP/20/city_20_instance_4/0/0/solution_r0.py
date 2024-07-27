import itertools
import math
from random import sample, shuffle, seed

# Define city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return math.dist(cities[city1], cities[city2])

# Heuristic method: Multi-Start Hyper-Heuristic Approach inspired solution
def find_best_tour():
    best_distance = float('inf')
    best_tour = []
    seed(0)  # For reproducibility

    # Generate random subsets of cities (excluding the depot city 0)
    for _ in range(1000):  # Number of random subsets to generate
        current_subset = sample(list(cities.keys())[1:], 15)  # 15 other cities
        current_subset.append(0)  # Include depot

        # Generate all permutations of the current city subset
        for perm in itertools.permutations(current_subset):
            if perm[0] != 0 or perm[-1] != 0:
                continue  # Ensure tour starts and ends at the depot
            # Calculate total travel cost of the permutation
            tour_cost = sum(distance(perm[i], perm[i+1]) for i in range(len(perm)-1))
            if tour_cost < best_distance:
                best_distance = tour_cost
                best_tour = perm

    return best_tour, best_distance

# Execute the heuristic search
best_tour, best_total_cost = find_best_tour()

# Output the results
print("Tour:", list(best_tour))
print("Total travel cost:", best_total_cost)