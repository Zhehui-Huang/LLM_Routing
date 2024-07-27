import math
from itertools import combinations, permutations

# City coordinates (depot + 9 other cities)
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 98),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all combinations of 3 additional cities to visit with the depot
city_combinations = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

# Initialize minimum cost and best tour tracking
min_cost = float('inf')
best_tour = []

# Check each combination
for combo in city_combinations:
    # Generate permutations for each combination to find the shortest path
    for permutation in permutations(combo):
        # Construct full tour starting and ending at depot city 0
        full_tour = [0] + list(permutation) + [0]

        # Calculate the total travel cost for this tour
        current_cost = sum(euclidean_distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))

        # Update the minimum cost and best tour if the current one is better
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = full_tour

# Output the best tour and the minimum travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")