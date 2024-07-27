import math
import itertools
from sys import maxsize

# Coordinates for each city
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Precompute distances between all pairs of cities
distances = {}
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            distances[(c1, c2)] = euclidean_distance(cities[c1], cities[c2])

# Function to calculate the total tour cost
def tour_cost(tour):
    return sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Generate all combinations of 12 cities (excluding the depot) to form a complete tour of 13 with the depot
def find_best_k_tsp_tour():
    min_tour = None
    min_cost = maxsize
    for comb in itertools.combinations([i for i in range(1, 20)], 12):
        # Generate all permutations of this combination set
        for perm in itertools.permutations(comb):
            perm_tour = [0] + list(perm) + [0]
            current_cost = tour_cost(perm_tour)
            if current_cost < min_cost:
                min_cost = current_cost
                min_tour = perm_tour
    return min_tour, min_cost

# Finding the best tour and cost
best_tour, best_cost = find_best_k_tsp_tour()

# Print the results directly
print(f"Tour: {best_tour}")
print(f"Total travel cost: {int(best_cost)}")