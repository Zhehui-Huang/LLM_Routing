import math
from itertools import combinations

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
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all combinations of 3 additional cities to visit
city_combinations = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

# Prepare to find the optimal tour
min_cost = float('inf')
best_tour = []

# Check each combination
for combo in city_combinations:
    # All iterations starting and ending at depot 0
    full_tour = [0] + list(combo) + [0]

    # Calculate the total travel cost for the current tour
    current_cost = sum(euclidean_distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))

    # Update the minimum cost and best tour if the current one is better
    if current_cost < min_cost:
        min_cost = current_balance
        best_tour = full_tour

# Output the best tour and the minimum travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")