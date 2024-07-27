import itertools
import math

# Cities coordinates with the depot as the first element
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Euclidean distance calculation
def calculate_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Generate all combinations of cities selecting one city from each group
all_possible_tours = itertools.product(*groups)

# Evaluate each possible tour by calculating total travel cost, starting and ending at depot
min_cost = float('inf')
best_tour = None

for tour in all_possible_tours:
    full_tour = [0] + list(tour) + [0]
    cost = sum(calculate_distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
    
    if cost < min_cost:
        min_cost = cost
        best_tour = full_tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")