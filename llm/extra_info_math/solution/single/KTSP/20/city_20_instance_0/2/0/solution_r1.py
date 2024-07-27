from itertools import combinations, permutations
import math

# Define the cities coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate combinations of 3 distinct cities (not including the depot)
city_indices = list(range(1, 20))  # Exclude depot
combinations_of_cities = list(combinations(city_indices, 3))

min_cost = float('inf')
best_tour = None

# Test each combination, generating tours starting and ending at depot
for comb in combinations_of_cities:
    # To ensure that all tours start and end at the depot
    test_tour = [0] + list(comb) + [0]
    for perm in permutations(comb):
        # Consider each permutation of city visits for thoroughness
        perm_tour = [0] + list(perm) + [0]
        cost = sum(euclidean_distance(perm_tour[i], perm_tour[i+1]) for i in range(len(perm_tour) - 1))
        if cost < min_cost:
            min_cost = cost
            best_tour = perm_tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel distance:", min_cost)