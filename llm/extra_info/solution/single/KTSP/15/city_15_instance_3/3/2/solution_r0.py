import itertools
from math import sqrt
import sys

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

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Generate combinations of 9 cities (excluding depot) out of the available cities
city_combinations = itertools.combinations(range(1, 15), 9)

min_cost = sys.maxsize
best_tour = None

for subset in city_combinations:
    # Always include the depot city in the tour
    current_subset = [0] + list(subset)
    
    # Generate all permutations of this subset of 10 cities to find the smallest tour possible
    for perm in itertools.permutations(current_subset):
        if perm[0] == 0 and perm[-1] == 0:  # Ensure the tour starts and ends at the depot
            cost = calculate_tour_cost(perm)
            if cost < min_cost:
                min_cost = cost
                best_tour = perm

# Output the solution
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {min_cost}")