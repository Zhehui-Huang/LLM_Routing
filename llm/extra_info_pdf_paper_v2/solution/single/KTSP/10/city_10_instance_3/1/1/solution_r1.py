import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean

# City coordinates
cities = np.array([
    (84, 67),  # depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
])

# Distance matrix calculation function
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

distance_matrix = calculate_distance_division(cities)


# Total cost calculator for a given tour
def total_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))


# Finding the best tour that visits exactly 7 cities starting and ending at the depot
best_tour = None
min_cost = float('inf')

# Generate all combinations of 7 cities including the depot
for subset in combinations(range(1, 10), 6):  # choose 6 additional cities besides the depot
    current_subset = [0] + list(subset) + [0]  # adding depot at start and end of tour

    # Permutate the chosen 7 cities (excluding first and last depot as they must remain fixed)
    for perm in permutations(current_subset[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_cost = total_tour_cost(current_tour, distance_matrix)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the best tour and the minimum cost found
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")