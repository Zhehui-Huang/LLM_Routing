import itertools
import math

# Coordinates of cities including the depot
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups, from which one city must be chosen
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all combinations of cities visiting one from each group
city_combinations = list(itertools.product(*city_groups.values()))

# Function to calculate the total path distance
def calculate_tour_distance(tour):
    total_distance = 0
    # Start at the depot, go through the cities and return to the depot
    path = [0] + list(tour) + [0]
    for i in range(len(path) - 1):
        total_distance += calculate_distance(path[i], path[i + 1])
    return total_distance

# Evaluate all possible tours to find the minimum distance
min_distance = float('inf')
best_tour = []

for combination in city_combinations:
    distance = calculate_tour_distance(combination)
    if distance < min_distance:
        min_distance = distance
        best_tour = combination

# Format the best tour to start and end at the depot city 0
formatted_tour = [0] + list(best_tour) + [0]

# Output the results
print(f"Tour: {formatted_tdddeistance: {min_distance}")