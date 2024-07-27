import itertools
import math
from random import shuffle

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
coordinates = {
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

# Parameters
k = 7  # Including the depot city (0)

# Possible subsets of cities that includes the depot and ensures length 7
city_indices = list(range(10))
subsets = [subset for subset in itertools.combinations(city_indices, k) if 0 in subset]

def calculate_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]])
    return total_cost

def find_best_tour_among_subsets(subsets):
    best_cost = float('inf')
    best_tour = []

    for subset in subsets:
        # Finding the best tour for this subset by trying all permutations
        all_permutations = itertools.permutations(subset)
        for permutation in all_permutations:
            if permutation[0] == 0 and permutation[-1] == 0:  # start and end at depot
                current_cost = calculate_route_cost(permutation)
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_tour = permutation

    return best_tour, best_cost

# Main execution to find the best tour
best_tour, best_tour_cost = find_best_tour_among_subsets(subsets)

# Output results
print("Tour:", list(best_tour))
print("Total travel cost:", round(best_tour_cost, 2))