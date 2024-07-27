import itertools
import math

# Coordinates of the cities
coordinates = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    (x1, y1), (x2, y2) = coordinates[c1], coordinates[c2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total tour cost
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Brute force over all combinations to find the shortest tour
best_tour = None
min_cost = float('inf')

for group_selection in itertools.product(*groups):
    # Create all possible permutations of selected cities from each group
    for permutation in itertools.permutations(group-_selection):
        tour = [0] + list(permutation) + [0]  # Start and end at the depot city 0
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")