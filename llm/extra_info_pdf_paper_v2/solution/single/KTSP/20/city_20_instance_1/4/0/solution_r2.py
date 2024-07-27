import math
import itertools

# Given city coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Total cities to include the depot (7 cities means 6 aside from the depot)
k = 6

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def calculate_total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Find the shortest path for 7 cities including the depot
min_tour = None
min_distance = float('inf')

# Iterate over combinations of selecting k cities from n-1 cities (excluding the depot)
for cities_combination in itertools.combinations(range(1, len(cities)), k):
    # All tours must start and end at depot (city 0), combine with depot
    for permutation in itertools.permutations(cities_combination):
        # Consider each permutation of the cities combination
        current_tour = [0] + list(permutation) + [0]
        current_distance = calculate_total_distance(current_tour)
        # Update the minimum tour and its distance
        if current_distance < min_distance:
            min_distance = current_distance
            min_tour = current_tour

# Output the results
print("Tour:", min_tour)
print("Total travel cost:", min_distance)