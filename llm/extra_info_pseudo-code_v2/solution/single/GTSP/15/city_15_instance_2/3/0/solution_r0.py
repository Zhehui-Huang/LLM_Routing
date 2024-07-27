import math
from itertools import permutations

# Define the cities and their coordinates
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

# Groups from the problem statement
city_groups = [
    [8, 12, 14],  # Group 0
    [7, 10, 11],  # Group 1
    [4, 6, 9],    # Group 2
    [1, 3, 13],   # Group 3
    [2, 5]        # Group 4
]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def compute_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible tours by selecting one city from each group and get the best one
best_tour = None
min_cost = float('inf')

for prod in permutations([0, 1, 2, 3, 4]):
    for selection in [g[prod[i]] for i, g in enumerate(city_groups)]:
        candidates = [0] + selection + [0]
        tour_cost = compute_tour_cost(candidates)
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = candidates

# Print the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)