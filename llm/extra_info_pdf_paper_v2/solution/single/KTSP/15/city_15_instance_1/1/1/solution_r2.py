import numpy as np
from itertools import permutations

# Define the cities with their coordinates
cities_coordinates = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Compute Euclidean distance between two points
def calculate_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate the tour cost given a list of indices
def tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(cities_coordinates[tour[i-1]], cities_coordinates[tour[i]])
    # Include the return to the depot
    total_cost += calculate_distance(cities_coordinates[tour[-1]], cities_coordinates[tour[0]])
    return total_cost

# Find the shortest tour that visits exactly 6 cities, starting and ending at the depot city 0
def find_shortest_tour():
    shortest_tour = None
    min_cost = float('inf')
    # Generate all permutations of 5 cities (besides the depot)
    all_city_indices = list(range(1, 15))
    for perm in permutations(all_city_indices, 5):
        current_tour = [0] + list(perm) + [0] # start and end at the depot
        current_cost = tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = current_tour
    return shortest_tour, min_cost

# Calculating the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)