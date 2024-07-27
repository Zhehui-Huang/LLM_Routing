import itertools
import math

# City positions
city_positions = [
    (79, 15), # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Groups of cities
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

def calculate_distance(pos1, pos2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def compute_tour_distance(tour):
    """ Compute the total distance of a tour """
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += calculate_distance(city_positions[tour[i - 1]], city_positions[tour[i]])
    # Return to the depot
    total_distance += calculate_distance(city_positions[tour[-1]], city_positions[tour[0]])
    return total_distance

# Compute all combinations of cities, taking one from each group
all_combinations = itertools.product(*city_groups)

min_distance = float('inf')
best_tour = []

# Find the best tour visiting one city from each group
for combination in all_combinations:
    # Start and end at the depot
    current_tour = [0] + list(combination) + [0]
    distance = compute_tour_distance(current_tour)
    if distance < min_distance:
        min_distance = distance
        best_tour = current_tour

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")