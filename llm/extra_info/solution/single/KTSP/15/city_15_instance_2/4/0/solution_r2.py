import numpy as np
from itertools import permutations, combinations
from math import sqrt

# City coordinates setup
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def calculate_distance(city1_idx, city2_idx):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1_idx]
    x2, y2 = cities[city2_idx]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_distance(tour):
    """Calculate total distance of a tour."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i + 1])
    total_distance += calculate_distance(tour[-1], tour[0])
    return total_distance

def find_shortest_tour():
    shortest_distance = float('inf')
    best_tour = None
    city_indices = list(cities.keys())[1:]  # Exclude the depot city [0]

    # Generate all combinations of 7 other cities to visit
    for subset in combinations(city_indices, 7):
        # Create potential tours (depot + 7 cities, back to depot)
        potential_tour = [0] + list(subset)
        # Generate all permutations of the selected cities
        for perm in permutations(potential_tour[1:]):
            tour = [0] + list(perm) + [0]
            distance = calculate_tour_distance(tour)
            if distance < shortest_distance:
                shortest_distance = distance
                best_tour = tour

    return best_tour, shortest_distance

# Find the shortest tour and calculate its total distance
shortest_tour, shortest_distance = find_shortest_tour()

# Print the best tour and its travel cost
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shorttext}")