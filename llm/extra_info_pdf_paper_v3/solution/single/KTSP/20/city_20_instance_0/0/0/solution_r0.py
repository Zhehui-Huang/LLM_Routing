import itertools
import math

# City coordinates
cities = {
    0: (8, 11),   # Depot city
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

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def calculate_total_distance(route):
    # Sum the distances between consecutive cities in the route, including return to the depot
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(route[i], route[i+1])
    return total_distance

# Generate all combinations of 3 cities excluding the depot
city_indices = list(cities.keys())[1:]  # exclude the depot from combinations
combinations = itertools.combinations(city_indices, 3)

# Find the minimum distance tour
min_distance = float('inf')
best_tour = None

for combination in combinations:
    # Create all permutations of the current combination
    permutations = itertools.permutations(combination)
    for permutation in permutations:
        # Construct the full tour: start at depot, visit the permutation, and return to depot
        tour = [0] + list(permutation) + [0]
        # Calculate the total distance of the tour
        distance = calculate_total_distance(tour)
        # Update the minimum distance and best tour if the current one is better
        if distance < min_distance:
            min_distance = distance
            best_tour = tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))