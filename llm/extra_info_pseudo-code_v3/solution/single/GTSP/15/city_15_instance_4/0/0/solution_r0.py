import itertools
from math import sqrt

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate the total tour distance
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

# Generate all possible tours and find the one with the minimum distance
min_distance = float('inf')
optimal_tour = None

for combination in itertools.product(*groups):
    full_tour = [0] + list(combination) + [0]  # Construct the full tour from depot and back
    distance = calculate_tour_distance(full_tour)
    if distance < min_distance:
        min_distance = distance
        optimal_tour = full_tour

# Output the optimal tour and its total travel cost
print('Tour:', optimal_tour)
print('Total travel cost:', min_distance)