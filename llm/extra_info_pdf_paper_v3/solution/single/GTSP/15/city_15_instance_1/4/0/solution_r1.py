import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities and their coordinates
cities = {
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
    14: (98, 1),
}

# Define city groups
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14],
]

# Find the shortest round trip that visits one city from each group and returns to the depot
min_cost = float('inf')
best_tour = []

# Generate all possible combinations of one city per group
for combination in itertools.product(*city_groups):
    # Create all permutations of the chosen cities
    for p in permutations(combination):
        # Start each tour from the depot, visit each city, and return to the depot
        tour = [0] + list(p) + [0]
        # Calculate the total travel cost of the tour
        total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        
        # Check if the new tour has a smaller cost
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")