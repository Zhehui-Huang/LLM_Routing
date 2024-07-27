import itertools
import math

# City coordinates
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

# Euclidean distance function
def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate all combinations of 12 cities from the 19 non-depot cities
all_combinations = itertools.combinations(range(1, 20), 12)

min_cost = float('inf')
best_tour = None

# Test all combinations
for combination in all_combinations:
    # Make a full tour including the depot
    current_combination = [0] + list(combination) + [0]
    # Generate all permutations of the selected cities
    for tour in itertools.permutations(combination):
        # Construct a complete tour by appending the depot at beginning and end
        complete_tour = [0] + list(tour) + [0]
        # Calculate total travel cost
        cost = sum(calculate_distance(complete_tour[i], complete_tour[i + 1]) for i in range(len(complete_tour) - 1))
        
        # Track the minimum cost and corresponding tour
        if cost < min_cost:
            min_cost = cost
            best_tour = complete_tour

# Output the best tour and its travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")