import itertools
import math

# Coordinates of the cities
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# City groups
city_groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all possible combinations; one city from each group
group_permutations = list(itertools.product(*city_groups))

# Function to calculate total distance of a tour
def total_tour_distance(tour):
    total_distance = calculate_distance(0, tour[0])  # Start from the depot to first city
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i + 1])
    total_distance += calculate_distance(tour[-1], 0)  # Return to the depot
    return total_distance

# Evaluate each tour combination and find the minimum distance tour
min_distance = float('inf')
best_tour = []

for group_combination in group_permutations:
    tour = [0] + list(group_combination) + [0]
    current_distance = total_tour_distance(group_combination)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = tour

# Output the best tour and the minimum distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")