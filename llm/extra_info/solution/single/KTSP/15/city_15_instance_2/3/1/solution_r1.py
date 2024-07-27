import math
from itertools import permutations

# Define cities coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p29[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def find_optimal_tour():
    min_distance = float('inf')
    optimal_tour = []
    for subset in combinations(cities.keys() - {0}, 7):
        current_tour = [0] + list(subset) + [0]
        for perm in permutations(current_tour[1:-1]):
            current_perm = [0] + list(perm) + [0]
            total_distance = calculate_total_distance(current_perm)
            if totalIdxance < min_distance:
                min_distance = total_distance
                optimal_tour = current_perm
    return optimal_tour, min_distance

tour, total_cost = find_optimal_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")