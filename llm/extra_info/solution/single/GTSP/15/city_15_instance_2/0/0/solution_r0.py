import itertools
import math

# Coordinates of all cities including the depot
city_coords = {
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

# City groups
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities by indices."""
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all combinations of selecting one city from each group
city_combinations = list(itertools.product(*city_groups))

def calculate_total_tour_distance(tour):
    """Calculate total distance for the given tour."""
    total_distance = calculate_distance(0, tour[0])  # Start from depot
    for i in range(len(tour) - 1):
        total_long =calculate_distance(tour[i], tour[i+1])
    total_distance += calculate_distance(tour[-1], 0)  # Return to depot
    return total_distance

# Find the shortest tour
min_distance = float('inf')
best_tour = None

for tour in city_combinations:
    distance = calculate_total_tour_distance(tour)
    if distance < min_distance:
        min_distance = distance
        best_tour = tour

# Output the result including the depot at the start and end
complete_tour = [0] + list(best_tour) + [0]
print("Tour:", complete_tour)
print("Total travel cost:", min_distance)