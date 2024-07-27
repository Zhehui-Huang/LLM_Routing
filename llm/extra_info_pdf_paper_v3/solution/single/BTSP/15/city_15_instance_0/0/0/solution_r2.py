import itertools
import math

# Coordinates of the cities
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def evaluate_tour(tour):
    total_distance = 0
    max_distance_between_cities = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_distance += dist
        if dist > max_distance_between_cities:
            max_distance_between_cities = dist
    return total_distance, max_distance_between_cities

best_tour = None
minimal_max_distance = float('inf')
best_total_distance = float('inf')

# Evaluating all permutations
for permutation in itertools.permutations(range(1, 15)):
    tour = [0] + list(permutation) + [0]
    total_distance, max_distance_between_cities = evaluate_tour(tour)
    if max_distance_between_cities < minimal_max_distance:
        best_tour = tour
        minimal_max_distance = max_distance_between_cities
        best_total_distance = total_distance

# Results
print("Tour:", best_tour)
print("Total travel cost:", best_total_distance)
print("Maximum distance between consecutive cities:", minimal_max_distance)