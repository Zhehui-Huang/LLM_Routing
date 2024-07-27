import itertools
import math

# Define the coordinates of the cities
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city_a, city_b):
    xa, ya = cities[city_a]
    xb, yb = cities[city_b]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# Finding the shortest tour visiting exactly 4 cities including the depot
min_cost = float('inf')
best_tour = []

# Consider combinations of 3 other cities since the depot city (0) must be included
for combo in itertools.combinations(range(1, 20), 3):
    # Include the depot city
    current_combination = (0,) + combo + (0,)
    # Test all permutations of this 4-city selection to find the minimum tour cost
    for perm in itertools.permutations(current_combination):
        if perm[0] == 0 and perm[-1] == 0:  # Ensure it starts and ends at the depot
            total_cost = sum(calc_distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour = list(perm)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)