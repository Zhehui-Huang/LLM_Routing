import math
import itertools

# Coordinates of the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def euclidean_distance(city1, city2):
    """Returns the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute all pairwise city distances
distances = {(i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j}

# Number of cities to visit including the depot
k = 6

# Find all combinations of k-1 cities (excluding the depot)
city_combinations = itertools.combinations([i for i in cities if i != 0], k - 1)

def calculate_tour_cost(tour):
    """Calculates the total travel cost of a given tour."""
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Search for the shortest tour
min_tour = None
min_cost = float('inf')

for comb in city_combinations:
    # We create tours that start and end at the depot city 0
    current_comb = (0,) + comb + (0,)
    for p in itertools.permutations(comb):
        current_tour = (0,) + p + (0,)
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            min_tour = current_tour

# Output the minimum cost tour found
print(f"Tour: {list(min_tour)}")
print(f"Total travel cost: {min_cost:.2f}")