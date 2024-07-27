import math
from itertools import product

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Grouping of cities
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

def euclidean_distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Pre-compute the minimal distances from the depot to each group and within each group
min_distance_to_depot = {group_id: min(euclidean_distance(0, city) for city in group) for group_id, group in enumerate(groups)}

# Function to calculate the round trip distance for a given tour
def calculate_total_distance(tour):
    total_distance = euclidean_distance(0, tour[0])  # From depot to first city in tour
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    total_distance += euclidean_distance(tour[-1], 0)  # From last city in tour back to depot
    return total_distance

# Generate all possible tours by selecting one city from each group
min_tour = None
min_tour_distance = float('inf')

for combination in product(*groups):
    tour_distance = calculate_total_distance(combination)
    if tour_distance < min_tour_distance:
        min_tour_distance = tour_distance
        min_tour = combination

# Output the results including the depot at the start and end of the tour
result_tour = [0] + list(min_tour) + [0]