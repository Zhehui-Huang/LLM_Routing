from itertools import product
import math

# Coordinates of the cities
city_locations = [
    (14, 77),  # City 0 - Depot
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Calculate Euclidean distance
def distance(city_a, city_b):
    x1, y1 = city_locations[city_a]
    x2, y2 = city_locations[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Evaluate the total tour cost
def evaluate_tour(tour):
    total_distance = distance(0, tour[0]) + distance(tour[-1], 0)
    total_distance += sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_distance

# Find the best tour
min_cost = float('inf')
best_tour = []

for combination in product(*groups):
    current_tour = [0] + list(combination) + [0]
    cost = evaluate_tour(list(combination))
    if cost < min_cost:
        min_cost = cost
        best_tour = current_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")