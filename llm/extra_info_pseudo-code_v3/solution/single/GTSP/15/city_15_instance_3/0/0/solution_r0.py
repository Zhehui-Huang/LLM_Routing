import itertools
import math

# Coordinates of the depot and cities
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Groups of cities
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Generate all possible tours by selecting one city from each group
possible_tours = list(itertools.product(*groups))

# Function to calculate total distance of the tour including return to the depot
def calculate_tour_distance(tour):
    # Start at depot, go through the tour, and return to depot
    full_tour = [0] + list(tour) + [0]
    total_distance = 0
    for i in range(len(full_tour) - 1):
        total_distance += euclidean_distance(full_tour[i], full_tour[i + 1])
    return total_distance

# Find the best tour with the minimum distance
shortest_distance = float('inf')
best_tour = None

for tour in possible_tours:
    current_distance = calculate_tour_distance(tour)
    if current_distance < shortest_distance:
        shortest_distance = current_distance
        best_turg options, config defaultitude comfort823]> = list(tour)

# Output results
best_tur = [0] + best_tour + [0]
print(f"Tour: {best_tour}")
print(f"Total travel cost: {shortest_distance}")