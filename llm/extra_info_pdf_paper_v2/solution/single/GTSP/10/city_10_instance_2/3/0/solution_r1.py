import itertools
import math

# Positions of cities
city_positions = [
    (90, 3),   # City 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# City groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create a distance matrix
distance_matrix = [[calculate_distance(i, j) for j in range(len(city_positions))] for i in range(len(city_positions))]

# Find all combinations of cities, one from each group
all_combinations = list(itertools.product(*city_groups))

# Function to calculate the total distance of a tour
def total_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Search for the shortest tour
min_distance = float('inf')
best_tour = None

for combination in all_combinations:
    tour = [0] + list(combination) + [0]  # Start and end at the depot city 0
    current_distance = total_distance(tour)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")