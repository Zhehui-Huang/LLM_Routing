import itertools
import math

# Coordinates of each city including the depot
coords = [
    (3, 26),  # Depot
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Grouping of cities
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# All possible combinations of cities, picking one from each group
all_combinations = itertools.product(*groups)

# Evaluate all combinations to find the shortest tour
best_tour = None
min_cost = float('inf')

for combination in all_combinations:
    current_tour = [0] + list(combination) + [0]  # start and end at the depot
    cost = sum(calculate_distance(coords[current_tour[i]], coords[current_tour[i+1]]) 
               for i in range(len(current_tour) - 1))
    
    if cost < min_cost:
        min_cost = cost
        best_tour = current_tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")