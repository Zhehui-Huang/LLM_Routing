import math
from itertools import permutations

# Provided city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities.
def dist(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate the total travel cost of a tour
def total_cost(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += dist(tour[i], tour[i + 1])
    return total

# Function to generate all potential tours visiting exactly k cities including start and end at the depot.
def k_tsp_tours(k):
    # Start with the depot city
    all_cities = set(cities.keys()) - {0}
    best_tour = None
    best_cost = float('inf')

    # Generate all subsets of size k-1 from the remaining cities since including the depot city
    for subset in permutations(all_cidsitties, k-1):
        current_tour = [0] + list(subset) + [0]  # Tour starting/ending at the depot
        cost = total_cost(current_tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = current_tour

    return best_tour, best_cost

# Optimal tour visiting 8 cities including the depot
optimal_tour, min_cost = k_tsp_tours(8)

print("Tour:", optimal_tour)
print("Total travel cost:", min_cost)