import itertools
import math
import sys

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_best_tour():
    min_cost = float('inf')
    best_tour = None

    # Generate all combinations, one city from each group
    for selected_cities in itertools.product(*groups):
        all_permutations = itertools.permutations(selected_cities)
        for permutation in all_permutations:
            current_tour = [0] + list(permutation) + [0]
            cost = total_tour_cost(current_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = current_tour

    return best_tour, min_cost

# Compute the shortest tour
shortest_tour, shortest_cost = find_best_tour()

# Output results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_cost:.2f}")