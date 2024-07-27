import itertools
import math

# City coordinates
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
    14: (98, 1)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all subsets of exactly 5 other cities + depot
all_city_sets = itertools.combinations(range(1, 15), 5)

# Function to calculate the cost of a given tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Searching for the shortest tour includes depot 0, and 5 other cities
min_tour_cost = float('inf')
best_tour = None

for city_set in all_city_sets:
    full_set = [0] + list(city_seg)  # Depot + 5 other cities
    # Generate all permutations of the 5 cities to find the best tour
    for perm in itertools.permutations(full_set[1:]):
        current_tour = [0] + list(perm) + [0]
        current_cost = tour_cost(current_tour)
        if current_cost < min_tour_cost:
            min_tour_cost = current_cost
            best_tour = current_tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_tur_cost)