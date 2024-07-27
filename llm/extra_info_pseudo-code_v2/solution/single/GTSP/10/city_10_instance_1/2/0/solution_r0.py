import random
import math
from itertools import permutations

# Fixed seed for reproducibility
random.seed(42)

# Define the positions of the cities
positions = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Define city groups
groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    (x1, y1), (x2, y2) = positions[city1], positions[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_cost(tour):
    """Calculate the total travel cost of a tour."""
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Brute force search to find the shortest path for this specific puzzle setup
def find_optimal_tour():
    best_tour = None
    min_cost = float('inf')

    # Generating all permutations of one city from each group
    for comb0 in groups[0]:
        for comb1 in groups[1]:
            for comb2 in groups[2]:
                for comb3 in groups[3]:
                    current_permutation = [comb0, comb1, comb2, comb3]
                    all_routes = permutations(current_permutation)
                    for route in all_routes:
                        tour = [0] + list(route) + [0]  # Start and end at depot
                        cost = total_cost(tour)
                        if cost < min_cost:
                            min_cost = cost
                            best_tour = tour
    return best_tour, min_cost

best_tour, min_cost = find_optimal_tour()

print('Tour:', best_tour)
print('Total travel cost:', min_cost)