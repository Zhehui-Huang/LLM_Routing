import itertools
import math

# Coordinates of the cities
coordinates = [
    (14, 77), # Depot City 0
    (34, 20), # City 1
    (19, 38), # City 2
    (14, 91), # City 3
    (68, 98), # City 4
    (45, 84), # City 5
    (4, 56),   # City 6
    (54, 82), # City 7
    (37, 28), # City 8
    (27, 45), # City 9
    (90, 85), # City 10
    (98, 76), # City 11
    (6, 19),  # City 12
    (26, 29), # City 13
    (21, 79), # City 14
    (49, 23), # City 15
    (78, 76), # City 16
    (68, 45), # City 17
    (50, 28), # City 18
    (69, 9)   # City 19
]

# Groups of cities
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_distance(tour):
    """Calculate the total distance of the given tour."""
    total_distance = 0
    # Start from the depot, visit each city, and return to the depot
    previous_city = 0
    for city in tour:
        total_distance += euclidean_distance(previous_city, city)
        previous_city = city
    total_distance += euclidean_distance(tour[-1], 0)  # Return to depot
    return total_distance

# Generate all combinations of one city from each group
all_combinations = itertools.product(*city_groups)
shortest_tour = None
min_distance = float('inf')

# Evaluate each combination tour
for combination in all_combinations:
    tour = [0] + list(combination)
    distance = calculate_total_distance(tour)
    if distance < min_distance:
        min_distance = distance
        shortest_tour = tour

# Adding the depot city again to the tour for the return trip
shortest_tour.append(0)

# Results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {round(min_distance, 2)}")