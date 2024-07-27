import math
from itertools import permutations

# City coordinates
cities = {
    0: (8, 11),
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

# Groupings of the cities
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all candidate tours
def candidate_tours(groups):
    all_combinations = list(permutations([group for group in groups.values()], len(groups)))
    best_distance = float('inf')
    best_tour = []
    
    for comb in all_combinations:
        for cities_comb in permutations(comb[0], 1):
            for cities_comb1 in permutations(comb[1], 1):
                for cities_comb2 in permutations(comb[2], 1):
                    tour = [0, cities_comb[0], cities_comb1[0], cities_comb2[0], 0]
                    total_distance = distance(tour[0], tour[1]) + distance(tour[1], tour[2]) \
                                     + distance(tour[2], tour[3]) + distance(tour[3], tour[4])
                    if total_distance < best_distance:
                        best_distance = total_distance
                        best_tour = tour
    
    return best_tour, best_distance

# Finding the shortest tour that visits one city from each group, starting and ending at the depot city
best_tour, best_cost = candidate_tours(groups)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")