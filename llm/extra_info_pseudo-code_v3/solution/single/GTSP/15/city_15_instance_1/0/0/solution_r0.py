from itertools import product, permutations
from math import sqrt

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of cities selecting one from each group
group_combinations = product(*groups)

# Find the tour with the minimum cost
min_cost = float('inf')
best_tour = None

for combination in group_combinations:
    # Include all permutations of the selected cities
    for perm in permutations(combination):
        # Calculate the cost of the tour starting and ending at the depot (city 0)
        tour = [0] + list(perm) + [0]
        tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        # Update the minimum cost and best tour if a new minimum is found
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")