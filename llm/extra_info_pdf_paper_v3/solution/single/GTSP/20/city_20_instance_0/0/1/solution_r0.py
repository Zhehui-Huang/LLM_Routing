import itertools
import math

# City coordinates from the given data
coordinates = [
    (8, 11),  # Depot city 0
    (40, 6),  # Group 0
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Groups given the city indices
groups = [
    [1, 3, 5, 11, 13, 14, 19],  # Group 0
    [2, 6, 7, 8, 12, 15],       # Group 1
    [4, 9, 10, 16, 17, 18]      # Group 2
]

# Function to compute Euclidean distance between two cities
def euclidean_distance(index1, index2):
    x1, y1 = coordinates[index1]
    x2, y2 = coordinates[index2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of one city from each group
all_combinations = list(itertools.product(*groups))

# Function to calculate total distance of the tour
def calculate_tour_distance(combination):
    # Start at depot, visit each city in combination order, return to depot
    tour = [0] + list(combination) + [0]
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Determine the shortest tour and its distance
min_distance = float('inf')
best_tour = None

for combination in all_combinations:
    tour_distance = calculate_tour_distance(combination)
    if tour_distance < min_distance:
        min_distance = tour_distance
        best_tour = combination

# Construct the final tour starting and ending at the depot
if best_tour:
    final_tour = [0] + list(best_tour) + [0]

# Output the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {min_distance}")