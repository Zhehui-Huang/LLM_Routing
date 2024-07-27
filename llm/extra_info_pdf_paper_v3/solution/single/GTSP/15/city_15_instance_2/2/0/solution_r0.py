import itertools
import math

# City coordinates (city index: coordinates)
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

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all permutations of one city from each group
possible_tours = itertools.product(*groups)

# Function to calculate the total distance of the tour starting and ending at the depot (city 0)
def total_tour_distance(tour):
    full_tour = [0] + list(tour) + [0]
    total_distance = 0
    for i in range(len(full_tour) - 1):
        total_distance += calculate_distance(full_tour[i], full_tour[i + 1])
    return total_distance

# Find the shortest tour
min_distance = float('inf')
best_tour = None

for tour in possible_tours:
    distance = total_tour_distance(tour)
    if distance < min_distance:
        min_distance = distance
        best_tour = tour

# Output the result
shortest_tour = [0] + list(best_tour) + [0]
print('Tour:', shortest_tour)
print('Total travel cost:', round(min_distance, 2))