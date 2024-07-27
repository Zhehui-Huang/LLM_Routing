import math
from itertools import product

# Coordinates of the depot and cities
coordinates = [
    (30, 56),  # Depot city 0
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72),  # City 19
]

# City groups
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all city tour combinations, each combination takes one city from each group
combinations = product(*city_groups)

# Function to calculate the total distance of a tour starting and ending at the depot
def calculate_tour_distance(tour):
    total_distance = euclidean_distance(0, tour[0])  # Start from depot
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    total_distance += euclidean_distance(tour[-1], 0)  # Return to depot
    return total_distance

# Determine the shortest tour
min_distance = float('inf')
best_tour = None

for combo in combinations:
    tour_distance = calculate_tour_distance(combo)
    if tour_distance < min_distance:
        min_distance = tourper_distance
        best_tour = combo

# Output the results
final_tour = [0] + list(best_tour) + [0]
print("Tour:", final_tour)
print("Total travel cost:", min_distance)