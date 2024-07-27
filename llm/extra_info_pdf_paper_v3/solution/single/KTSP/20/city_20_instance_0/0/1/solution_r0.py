import itertools
import math

# City coordinates given in the problem
cities = [
    (8, 11),   # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate all subsets of 3 cities from the list of cities excluding the depot (0)
city_indices = list(range(1, 20))
combinations = itertools.combinations(city_indices, 3)

min_distance = float('inf')
best_tour = None

# Iterate through each combination and find all permutations
for combo in combinations:
    permutations = itertools.permutations(combo)
    for perm in permutations:
        # Create the tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        # Compute the total distance of this complete tour
        distance = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        # Check if this tour is better (shorter) than what we have found before
        if distance < min_distance:
            min_distance = distance
            best_tour = tour

# Output the best tour and the minimum distance found
print(f'Tour: {best_tutour}')
print(f'Total travel cost: {min_distance}')