import itertools
from math import sqrt
import sys

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate total travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Generate combinations of 9 non-depot cities to visit
city_combinations = itertools.combinations(range(1, 15), 9)

min_cost = sys.maxsize
best_tour = None

# Iterate through each city combination
for subset in city_combinations:
    # Append the depot to the start and end of each tour
    current_subset = [0] + list(subset) + [0]
    
    # Generate all permutations of the remaining cities in the tour
    for perm in itertools.permutations(current_subset[1:-1]):
        tour = [0] + list(perm) + [0]
        if tour[0] == 0 and tour[-1] == 0:  # Ensures the tour starts and ends at the depot
            cost = calculate_tour_cost(tour)
            if cost < min_cost:
                min_tour = tour
                min_cost = cost

# Output the solution
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost}")