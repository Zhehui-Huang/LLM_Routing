import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour, city_positions):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
    return total_distance

# City positions
city_positions = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62),
    (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# City groups
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Generating all possible tours
all_possible_group_choices = list(itertools.product(*city_groups))
all_possible_tours = [[0] + list(choice) + [0] for choice in all_possible_group_choices]

# Find the shortest tour
shortest_distance = float('inf')
best_tour = None

for tour in all_possible_tours:
    distance = calculate_total_distance(tour, city_positions)
    if distance < shortest_distance:
        shortest_distance = distance
        best_tour = tour

# Result
shortest_distance = round(shortest_distance, 2)  # Rounding for cleaner output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {shortest_distance}")