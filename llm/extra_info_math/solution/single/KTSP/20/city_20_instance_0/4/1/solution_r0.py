import itertools
import math

# Define cities and their coordinates
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
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to calculate the total travel cost for a specific city tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(tour[i - 1], tour[i])
    return total_cost

# Include the depot city (0) and pick all combinations of exactly 3 other cities
min_cost = float('inf')
best_tour = []

for comb in itertools.combinations(range(1, 20), 3):
    # Cycle through permutations of the chosen city subset including return to depot
    for perm in itertools.permutations(comb):
        current_tour = [0] + list(perm) + [0]
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the best tour found and the corresponding travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))