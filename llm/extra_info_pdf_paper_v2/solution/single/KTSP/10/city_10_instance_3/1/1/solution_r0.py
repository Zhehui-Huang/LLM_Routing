import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean

# City coordinates
cities = np.array([
    (84, 67),
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

# Calculate distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance = euclidean(cities[i], cities[j])
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

# Initialize required variables
k = 7  # We need to select 7 total cities including the depot

# Choose the initial subset (starting simple: choose the first k cities for initialization)
initial_subset = list(range(k))

def total_tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i], tour[i+1]]
    return cost

# Initial tour by permuting the initial subset and re-adding the depot city
best_tour = None
min_cost = float('inf')

# Generate all k-1 factorial permutations of the 6 city indices other than the depot
for perm in permutations(initialed_subset[1:]):
    current_tour = [0] + list(perm) + [0]
    current_cost = total_tour_cost(current_tour, distance_matrix)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

# Simple Local Search to potentially improve the initial solution
# Swapping cities within the tour to find better options
improved = True
while improved:
    improved = False
    for i in range(1, k-1):  # Ignore swapping the depot (index 0)
        for j in range(i+1, k):
            new_tour = best_tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = total_tour_cost(new_tour, distance_matrix)
            if new_cost < min_cost:
                min_cost = new_cost
                best_tour = new_tour
                improved = True

# Output the best tour found and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")