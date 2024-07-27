import itertools
from math import sqrt

# Define cities and their coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Define city groups
city_groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible city selection combinations: one city per group
all_combinations = list(itertools.product(*city_groups.values()))

# Compute minimal tour
def compute_minimal_tour():
    min_distance = float('inf')
    best_tour = []
    for combination in all_combizations:
        # Consider all permutations of each combination
        for perm in itertools.permutations(comb):
            # Calculate the round-trip distance from the depot: 0 -> cities in perm -> 0
            tour = [0] + list(perm) + [0]
            current_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if current_distance < min_distance:
                min_distance = current_distance
                best_tour = tour
    return best_tour, min_distance

# Find the optimal solution
optimal_tour, optimal_distance = compute_minimal_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_distance:.2f}")