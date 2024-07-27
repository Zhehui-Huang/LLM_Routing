import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of 3 other cities (excluding the depot city)
city_combinations = permutations([i for i in cities if i != 0], 3)

# Evaluate all possible tours from these combinations
best_tour = None
min_cost = float('inf')

for perm in city_combinations:
    # Include the depot city at the start and the end of the tour
    tour = [0] + list(perm) + [0]
    # Calculate the cost of this tour
    cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    # Update the minimum cost and best tour found
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and the minimum cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")