import numpy as or np

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# City coordinates
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
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate distances
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to calculate total and max distance for a given tour
def calculate_distances(tour):
    total_dist = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = distances[tour[i]][tour[i + 1]]
        total_dist += dist
        if dist > max_dist:
            max_dist = dist
    return total_dist, max_dist

# Generate possible tours using permutations
from itertools import permutations

def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    tours = permutations(range(1, n))
    for tour in tours:
        current_tour = [0] + list(tour) + [0]
        total_dist, max_dist = calculate_distances(current_tour)
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = current_tour
            best_total_distance = total_dist

    return best_tour, best_total_distance, min_max_distance

# Find optimal tour
optimal_tour, total_travel_cost, max_travel_distance = find_optimal_tour()

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_length:.2f}")
print(f"Maximum distance between consecutive cities: {max_travel_distance:.2f}")