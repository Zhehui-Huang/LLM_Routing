import itertools
import math

# City coordinates including the depot city
coordinates = [
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

# Groups of cities
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Generate all combinations (one from each group)
combinations = list(itertools.product(*groups))

# Function to calculate the total travel cost of the tour
def calculate_tour_cost(tour):
    total_distance = euclidean_distance(0, tour[0])  # from depot to first city
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    total_distance += euclidean_distance(tour[-1], 0)  # from last city back to depot
    return total_distance

# Find the combination with the shortest tour
min_distance = float('inf')
best_tour = None

for combination in combinations:
    tour = [0] + list(combination) + [0]  # starting and ending at the depot city
    current_distance = calculate_tour_cost(list(combination))
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = tour

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")