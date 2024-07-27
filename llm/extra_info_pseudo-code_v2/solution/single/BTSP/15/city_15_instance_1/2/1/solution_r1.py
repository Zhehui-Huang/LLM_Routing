import math
import itertools

# Given city coordinates
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
    14: (98, 1),
}

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours that return to the starting city
def all_possible_tours(start_city):
    other_cities = list(cities.keys())
    other_cities.remove(start_city)
    for perm in itertools.permutations(other_cities):
        yield [start_city] + list(perm) + [start_city]

# Find the optimal tour minimizing the maximum distance between consecutive cities
def find_optimal_tour():
    best_tour = None
    best_max_distance = float('inf')
    for tour in all_possible_tours(0):
        max_distance = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        if max_distance < best_max_distance:
            best_tour = tour
            best_max_distance = max_distance
    return best_tour, best_max_distance

# Calculate total travel cost of the tour
def total_travel_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Main calculation
optimal_tour, max_distance_in_tour = find_optimal_tour()
total_cost = total_travel_cost(optimal_tour)

# Output results
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance_in_tour)