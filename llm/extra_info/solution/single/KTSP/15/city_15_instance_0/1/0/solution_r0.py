import itertools
import math

# City coordinates: city index is also the list index
cities = [
    (9, 93),  # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute pairwise distances between all cities
distances = {}
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        distance = euclidean_distance(cities[i], cities[j])
        distances[frozenset([i, j])] = distance

# Generate combinations of 3 cities excluding the depot
other_cities = list(range(1, 15))
city_combinations = itertools.combinations(other_cities, 3)

# Find the shortest tour visiting exactly 4 cities
min_cost = float('inf')
best_tour = None
for comb in city_combinations:
    current_comb = [0] + list(comb)
    for perm in itertools.permutations(current_comb[1:]):
        tour = tuple([0] + list(perm) + [0])
        # Calculate total travel cost for this permutation
        cost = 0
        for k in range(len(tour) - 1):
            cost += distances[frozenset([tour[k], tour[k+1]])]
        # Update the minimum cost
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {min_cost:.2f}")