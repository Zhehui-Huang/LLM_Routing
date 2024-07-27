import math
import itertools

# Define cities and their positions
positions = {
    0: (30, 56), # Depot
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Define city groups
groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Function to calculate Euclidean distance
def distance(a, b):
    return math.sqrt((positions[a][0] - positions[b][0])**2 + (positions[a][1] - positions[b][1])**2)

# Generate all combination of one city per group
group_permutations = list(itertools.product(*groups.values()))

def total_path_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i+1])
    total_distance += distance(tour[-1], tour[0])  # returning to the depot
    return total_distance

# Testing all combinations to find the best tour
best_distance = float('inf')
best_tour = None

for perm in group_permutations:
    tour = [0] + list(perm) + [0]
    current_distance = total_path_distance(tour)
    if current_distance < best_distance:
        best_distance = current_distance
        best_tour = tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", best_distance)