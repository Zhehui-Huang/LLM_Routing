import itertools
import math
from sys import float_info

# Define cities' coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate all pairwise distances between cities
distances = {}
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            distances[(c1, c2)] = distance(c1, c2)

# Heuristic function to find minimum tour
def find_tsp_tour():
    best_tour = []
    min_cost = float_info.max
    # n choose k-1 because k includes the depot city
    city_choices = itertools.combinations([i for i in cities.keys() if i != 0], 6)
    
    for subset in city_choices:
        # Include the depot city in the subset
        full_tour = [0] + list(subset) + [0]
        # Find all permutations of the chosen cities
        for tour in itertools.permutations(full_tour[1:-1]):
            tour = [0] + list(tour) + [0]
            cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tour, min_cost

# Get the best tour and its cost
best_tour, total_cost = find_tsp_tour()

# Output result
print("Tour:", best_tour)
print("Total travel cost:", total_cost)