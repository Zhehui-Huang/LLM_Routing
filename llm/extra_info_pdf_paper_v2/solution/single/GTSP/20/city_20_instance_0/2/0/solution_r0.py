from itertools import product
from math import sqrt

# City coordinates data
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

def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate all permutations of tours
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None

    for tour in product(groups[0], groups[1], groups[2]):
        tour_permutations = [tour[i:] + tour[:i] for i in range(len(tour))]  # All rotations of the tours
        for perm in tour_permutations:
            tour_with_depot = [0] + list(perm) + [0]  # Add starting and ending at the depot
            total_distance = sum(euclidean_distance(tour_with_depot[i], tour_with_depot[i + 1]) for i in range(len(tour_with_depot) - 1))
            
            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = tour_with_depot

    return best_tour, min_distance

best_tour, min_distance = find_shortest_tour()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")