import itertools
import math

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    6: (6, 61),
    14: (32, 79),
    5: (34, 73),
    12: (70, 95),
    13: (29, 64),
    7: (86, 69),
    10: (42, 64),
    4: (54, 93),
    11: (64, 30),
    2: (80, 21),
    8: (30, 50),
    3: (86, 92),
    9: (35, 73)
}

# City groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def evaluate_tour(tour):
    total_distance = calculate_distance(0, tour[0])  # Starting from the depot
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i+1])
    total_distance += calculate_distance(tour[-1], 0)  # Returning to the depot
    return total_distance

# Generate all combinations of cities, taking one from each group
all_tours = itertools.product(*groups)

# Find the shortest tour
min_distance = float('inf')
best_tour = None

for tour in all_tours:
    tour_distance = evaluate_tour(tour)
    if tour_distance < min_distance:
        min_distance = tour_distance
        best_tour = tour

# Add the depot to the tour
final_tour = [0] + list(best_tour) + [0]

# Output the results
print("Tour:", final_tour)
print("Total travel cost:", min_distance)