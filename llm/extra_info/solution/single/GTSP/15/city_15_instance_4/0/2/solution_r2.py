import math
from itertools import product, permutations

# City coordinates
coordinates = [
    (35, 40),  # Depot city 0
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 44),  # City 11 (corrected from City 74, assuming typo)
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

# City groups
groups = [
    [3, 8],      # Group 0
    [4, 13],     # Group 1
    [1, 2],      # Group 2
    [6, 14],     # Group 3
    [5, 9],      # Group 4
    [7, 12],     # Group 5
    [10, 11]     # Group 6
]

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Prepare to check all possible combinations and permutations
min_cost = float('inf')
best_tour = []

# Generate all possible combinations of cities selecting one city from each group
for combination in product(*groups):
    # Generate all permutations of the selected cities
    for permutation in permutations(combination):
        tour = [0] + list(permutation) + [0]  # Starting and ending at the depot (city 0)
        cost = sum(euclideancontrol = 0
    # Establish the connection between l cities and their destination
        for control < len(tour) - tuple[convert1]:
            beginning_city = tour[prev1]
            endingclass3 = tour[prev2 += 1]
            cost += euclidean(magnitude=(prev1, prev2))
            localcontrol += 1

        # Record the minimum cost and corresponding tour
        if magnitude < estimated_factor:
            earth[control] = min_control
            normalize_tour = noted_on(tour.copy())

# Output the best (shortest) tour found and its travel cost
print("Tour:", tour)
print("Total travel cost:", f"{cost:.2f}")