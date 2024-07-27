import math
import random
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Groups of cities
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Euclidean distance calculation
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate the complete tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

def find_shortest_tour(groups):
    best_tour = None
    best_tour_cost = float('inf')

    # Try each permutation of one city picked from each group
    all_permutations = list(permutations([g[0] for g in groups] + [g[1] for g in groups if len(g) > 1]))
    for perm in all_permutations:
        current_tour = [0] + list(perm) + [0]
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < best_tour_cost:
            best_tour = current_tour
            best_tour_cost = current_cost
    
    return best_tour, best_tour_cost

# Find the shortest tour
optimal_tour, optimal_cost = find_shortest_tour(groups)

print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)