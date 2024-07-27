import math
from itertools import permutations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# List of cities with their coordinates
cities = [
    (8, 11),   # Depot city 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# The robot needs to visit exactly 4 cities, including the depot city
# The tours should start and end at the depot city 0
min_cost = float('inf')
best_tour = None

# Generate all combinations of 3 additional cities (since the robot visits 4 including depot)
for comb in permutations(range(1, 20), 3):  # 19 cities excluding the depot
    tour = [0] + list(comb) + [0]  # construct the full tour starting and finishing at depot
    cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")