from itertools import product, permutations
from math import sqrt

# Define the cities
cities = {
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

# Define city groups
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all combinations of choosing one city from each group
all_group_combinations = list(product(*groups))

# Find the shortest path that includes one city from each group
min_cost = float('inf')
best_tour = None

for combination in all_group_combinations:
    # We check all permutations of the chosen cities
    for perm in permutations(combination):
        # Include the return to the depot city (both start and end)
        tour = [0] + list(perm) + [0]
        # Calculate the tour cost
        current_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = tour

# Output the best tour and the corresponding cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")