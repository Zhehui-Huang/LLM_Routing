import math
from itertools import product

# Coordinates for depot and cities
city_positions = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# City groups
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def euclidean_distance(city1, city2):
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_distance(tour):
    total_distance = euclidean_distance(0, tour[0])  # Start from depot
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    total_distance += euclidean_distance(tour[-1], 0)  # Return to depot
    return total_distance

# Generate all possible combinations of one city from each group
all_combinations = product(*city_groups)

# Initialize variables to track the best (shortest) tour found
min_distance = float('inf')
best_tour = None

# Evaluate each combination
for combination in all_combinations:
    tour = [0] + list(combination) + [0]  # Forming the complete tour
    total_distance = calculate_total_distance(combination)
    
    if total_distance < min_distance:
        min_distance = total_distance
        best_tour = tour

# Output the best tour and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")