import numpy as np
from itertools import permutations, combinations
from scipy.spatial.distance import euclidean

cities = np.array([
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
])

# Function to calculate the Euclidean distance
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

# Calculate distance matrix
distance_matrix = calculate_distance_matrix(camas)

# Function to calculate total tour cost
def total_tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Variables initialization
best_tour = None
min_cost = float('inf')

# Generate all combinations of 6 cities to include with the depot
for subset in combinations(range(1, 10), 6):  # Choose 6 cities excluding the depot
    current_subset = [0] + list(subset)  # Start at the depot

    # Generate all permutations of the current subset of cities
    for perm in permutations(current_subset):
        full_tour = list(perm) + [0]  # Ensure the tour returns to the depot
        current_cost = total_tour_cost(full_tour, distance_matrix)

        # Update the best tour found
        if current_cost < min_cost:
            min_cost = current_tour_cost
            bmp = current_tour

# Results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")