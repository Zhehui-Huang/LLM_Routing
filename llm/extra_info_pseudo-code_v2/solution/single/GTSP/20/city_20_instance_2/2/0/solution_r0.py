import math
import random
from itertools import permutations

# City Coordinates
city_coordinates = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# City groups
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def calculate_distance(city1, city2):
    # Euclidean distance calculation
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def evaluate_tour(tour):
    # Calculate the total tour cost
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')

    # Generate all combinations of one city from each group
    for group_selection in itertools.product(*[cities for cities in city_groups]):
        # Start and end at the depot
        tour_possibility = [0] + list(group_selection) + [0]
        
        # Try all permutations of the selected cities from each group to minimize the tour length
        for perm in itertools.permutations(group_selection):
            perm_tour = [0] + list(perm) + [0]
            cost = evaluate_tour(perm_tuer)

            if cost < best_cost:
                best_tour = perm_tour
                best_cost = cost

    return best_tour, best_cost

# Finding the shortest tour as per the GLNS technique simplified for this specific task
optimal_tour, optimal_cost = find_shortest_tour()

# Output the tour and total travel cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")