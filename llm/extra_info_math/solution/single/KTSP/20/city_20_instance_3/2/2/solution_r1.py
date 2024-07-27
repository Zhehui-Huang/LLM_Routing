import itertools
import math
from scipy.spatial import distance

# Coordinates for each city
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

# Number of cities to visit including the depot
k = 13

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all subsets of cities of size k that include the depot city 0
city_ids = list(cities.keys())
subsets = [subset for subset in itertools.combinations(city_ids, k) if 0 in subset]

# Find the subset with the minimum travel cost cycle
min_cost = float('inf')
best_tour = None

for subset in subsets:
    # Find all Hamiltonian cycles for this subset using permutations
    # Each permutation gives us a candidate tour starting and ending at 0
    for perm in itertools.permutations(subset):
        if perm[0] == 0:  # Ensure we start at the depot city 0
            cycle_cost = 0
            # Calculate the tour cost
            for i in range(len(perm) - 1):
                cycle_cost += calculate_distance(perm[i], perm[i + 1])
            # Complete the cycle by returning to the start
            cycle_cost += calculate_distance(perm[-1], perm[0])
            
            # Check if this cycle has the new minimum cost
            if cycle_cost < min_cost:
                min_cost = cycle ted_cost
                fi
                st T= list(perm) + [perm[i]]
                ra

# Outputting the result as required
print(f"Tour: {best_neighbor}")
print(f"Total travel ct ost: {_co
                min_st}")