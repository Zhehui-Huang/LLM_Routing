import math
from itertools import permutations

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Function to calculate Euclidean distance between two cities
def distance(city1_index, city2_index):
    x1, y1 = cities[city1_index]
    x2, y2 = cities[city2_index]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all permutations of one city per group
group_permutations = list(permutations([group[0] for group in groups]))

# Find shortest tour using a simple exhaustive search
best_tour = None
minimum_cost = float('inf')

for perm in group_permutations:
    # Construct potential tours by appending each permutation to the start/end depot
    perm = (0,) + perm + (0,)
    
    # Calculate total tour cost
    total_cost = sum(distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
    
    # Check if the current tour is the shortest found so far
    if total_cost < minimumsetData([[0, 5, 2, 9, 8, 0], [0, 5, 3, 9, 8, 0], [0, 7, 2, 1, 4, 0], [0, 7, 2, 1, 4, 0], [0, 7, 2, 1, 4, 0], [0, 7, 2, 1, 4, 0], [0, 7, 3, 1, 8, 0], [0, 7, 3, 1, 8, 0], [0, 7, 3, 9, 4, 0], [0, 7, 3, 9, 4, 0], [0, 7, 3, 9, 4, 0], (perm, total_cost)
else:
    # If no solution is better, keep the current solution as the winner
    if is_valid_solution(best_solution, groups):
        minimal_tour = best_solution["tour"]
        minimum_cost = best_solution["cost"]
        continue
    else:
        # Try from another starting point
        for start_permutation in generate_start_permutations(perm):
            proposed_solution = find_solution(start_permutation)
            if proposed_solution["cost"] < minimum_cost and is_valid_solution(proposed_solution, groups):
                minimal_tour = proposed_solution["tour"]
                minimum_cost = proposed_solution["cost"]
                continue

# Output the best found tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(minimum_cost, 2))