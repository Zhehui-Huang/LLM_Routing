import numpy as np
from itertools import permutations

# Given city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate all possible subsets of k-1 cities (excluding city 0)
def get_city_subsets(k, n):
    from itertools import combinations
    return [list(comb) for comb in combinations(range(1, n), k - 1)]

# Calculate tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Find the shortest possible tour
def find_optimal_tour():
    subsets = get_city_subsets(16, len(cities))  # Generate subsets of 15 cities excluding the depot (city 0)
    best_tour = None
    best_cost = float('inf')

    for subset in subsets:
        # Consider all permutations of the selected city subset
        for perm in permutations(subset):
            tour = [0] + list(perm) + [0]  # Construct a complete tour
            cost = calculate_tour_cost(tour)
            if cost < best_cost:
                best_tour = tour
                best_cost = cost

    return best_tour, best_cost

# Execute the function to find and print the optimal tour and its cost
optimal_tour, optimal_cost = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)