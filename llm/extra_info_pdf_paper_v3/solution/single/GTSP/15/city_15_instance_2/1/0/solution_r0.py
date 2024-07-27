import math
from itertools import permutations

# City coordinates
coordinates = [
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Pre-calculate all distances
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Generate all possible combinations of cities taking one from each group
from itertools import product

all_combinations = list(product(*groups))

# Function to calculate the total travel cost of a tour
def calculate_total_cost(tour):
    total_cost = 0
    current_city = 0  # start at the depot
    for city in tour:
        total_cost += distances[current_city][city]
        current_city = city
    total_cost += distances[current_city][0]  # go back to the depot
    return total_cost

# Find the tour with the minimum distance
best_tour = None
min_cost = float('inf')

for combination in all_combinations:
    # Try all permutations of the selected cities combination as the tour order might affect the total distance
    for perm in permutations(combination):
        cost = calculate_total_cost(perm)
        if cost < min_total_cost:
            best_tour = perm
            min_total_cost = cost

# Preparing the output in the required format
output_tour = [0] + list(best_tour) + [0]
output_cost = min_total_cost

print("Tour:", output_tour)
print("Total travel cost:", output_cost)