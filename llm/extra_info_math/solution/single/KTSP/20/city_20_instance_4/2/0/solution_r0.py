import math
import itertools

# Given coordinates of cities including the depot city
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Total cities chosen is 16 (0 to 15) plus depot city, mix and match others
total_cities = 16
subset_size = total_cities - 1  # Exclude depot deliberately since it must be included

# Compute all combinations of k-1 cities, since depot is always included
combinations = itertools.combinations(range(1, len(cities)), subset_size)

# Tour and minimal tour length initialisation
minimal_tour_length = float('inf')
best_tour = []

# Evaluate each combination
for combination in combinations:
    # Always start and end at depot, therefore include 0 in the sequence
    current_combination = [0] + list(combination)
    
    # Considering all permutations of current combination because we need the minimum cycle
    # Starting and ending at the depot
    for perm in itertools.permutations(current_combination[1:]):
        tour = [0] + list(perm) + [0]
        tour_length = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        
        # Check if this permutation gives a smaller tour length
        if tour_length < minimal_tour_length:
            minimal_tour_length = tour_length
            best_tour = tour

# Output results
print("Tour:", best_tour)
print("Total travel cost:", minimal_tour_length)