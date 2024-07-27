from itertools import permutations
import math

# Given city coordinates
cities = {
    0: (84, 67),  # Depot
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Evaluate total distance for a proposed tour
def evaluate_tour(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(tour[i], tour[i+1])
    return total_dist

# Generate all combination of cities selecting one from each group
all_possible_tours = permutations([group[0] for group in groups])

# Find the shortest tour by brute force search
min_distance = float('inf')
best_tour = None

for comb in all_possible_tours:
    for perm in permutations(comb):
        current_tour = [0] + list(perm) + [0]
        current_distance = evaluate_tour(current_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")