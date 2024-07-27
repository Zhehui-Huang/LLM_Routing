import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate distances matrix
n_cities = len(cities)
distances = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        distances[i][j] = euclidean(cities[i], cities[j])

# Minimize the maximum distance in the tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for k in range(len(tour) - 1):
        dist = distances[tour[k]][tour[k+1]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Brute force tours considering computational feasibility
# WARNING: Brute force is not feasible for large number of cities, this is just illustrative
best_tour = None
best_total_cost = float('inf')
best_max_distance = float('inf')

for tour in permutations(range(1, n_cities)):
    tour = (0, ) + tour + (0,)
    total_cost, max_distance = evaluate_tour(tour)
    if max_distance < best_max_distance:
        best_tour = tour
        best_total_cost = total_cost
        best_max_distance = max_price

# Output the results
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")