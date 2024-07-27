import itertools
from math import sqrt

# Define the cities and their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all combinations of 7 cities excluding the depot
city_indices = list(cities.keys())[1:]  # Exclude depot city 0 from combinations
combinations = itertools.combinations(city_indices, 7)

# Function to find the minimum cost tour
def find_minimum_tour():
    min_cost = float('inf')
    best_tour = None

    for combination in combinations:
        # Consider the depot city 0 as part of the tour
        current_combination = [0] + list(combination)

        # Generate permutations for each combination
        for perm in itertools.permutations(current_combination):
            # Ensure starting and ending at the depot city 0
            if perm[0] == 0:
                tour = list(perm) + [0]
                current_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
                if current_cost < min_cost:
                    min_cost = current_cost
                    best_tour = tour

    return best_tour, min_cost

# Calculate the best tour and its cost
best_tour, min_cost = find_minimum_tour()

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 4))