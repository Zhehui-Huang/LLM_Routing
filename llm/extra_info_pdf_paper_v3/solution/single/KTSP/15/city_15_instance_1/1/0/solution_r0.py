import itertools
import math
import random

# Given cities' coordinates
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
    14: (98, 1)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i+1])
    return total_distance

# Start at city 0, choose 5 cities from available 14 (excluding the depot)
def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    all_cities = list(cities.keys())[1:]  # exclude the depot for the choices
    for subset in itertools.combinations(all_cities, 5):
        current_tour = [0] + list(subset) + [0]  # Construct tour from the subset
        permutations = itertools.permutations(list(subset))
        for perm in permutations:
            permuted_tour = [0] + list(perm) + [0]
            cost = evaluate_tour(permuted_tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = permuted_tour
    
    return best_tour, best_cost

# Running the heuristic function to generate the best tour and cost
best_tour, best_cost = find_best_tour()

print("Tour:", best_tour)
print("Total travel cost:", best_cost)