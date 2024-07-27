import math
from itertools import product

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

city_groups = [
    [2, 7, 10, 11, 14],  # Group 0
    [1, 3, 5, 8, 13],    # Group 1
    [4, 6, 9, 12]        # Group 2
]

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate all possible tours considering one city from each group
possible_tours = []
for selection in product(*city_groups):
    possible_tour = [0] + list(selection) + [0]
    possible_tours.append(possible_tour)

# Evaluate all possible tours and find the one with the minimal travel cost
best_tour = None
min_cost = float('inf')

for tour in possible_tours:
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")