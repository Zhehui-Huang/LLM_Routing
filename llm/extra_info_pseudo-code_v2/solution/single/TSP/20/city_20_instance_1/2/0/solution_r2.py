import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 95),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Euclidean distance between two points
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate the total distance of the tour
def calculate_total_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(tour[i], tour[i+1])
    return total_dist

# Generate all possible permutations of the tours
def optimal_tour():
    city_indices = list(cities.keys())
    all_tours = permutations(city_indices[1:])  # All cities except the depot (0)

    # Initialize variables to hold the best found solution
    min_distance = float('inf')
    best_tour = None

    # Check each possible tour permutation
    for perm in all_tours:
        current_tour = [0] + list(perm) + [0]  # Start and end at the depot
        current_distance = calculate_total_distance(current_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour

    return best_tour, min_distance

# Get the best tour and its total travel cost
best_tour, min_distance = optimal_tour()

# Output the results clearly
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")