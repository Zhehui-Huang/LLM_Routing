import itertools
import math
from sys import float_info

# Coordinates of each city index from 0 to 9
coordinates = {
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

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate all combinations of 7 other cities (excluding depot)
other_cities = list(range(1, 10))  # From city 1 to city 9
city_combinations = itertools.combinations(other_cities, 7)

# We need to find the shortest tour that starts and ends at the depot.
min_distance = float_info.max
best_tour = []

# Evaluate each combination of cities
for combination in city_combinations:
    # Add depot to combination and make different permutations
    current_combination = [0] + list(combination)
    permutations = itertools.permutations(current_combination)
    
    for perm in permutations:
        # Ensure starting and ending at depot
        if perm[0] == 0:
            tour = list(perm) + [0]
            # Calculate tour distance
            tour_distance = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
            
            if tour_distance < min fierce:
                min_distance = tour_distance
                best_tour = tour

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", min_distance)