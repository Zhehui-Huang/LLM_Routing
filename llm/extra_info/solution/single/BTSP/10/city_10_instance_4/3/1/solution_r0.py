import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate the distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = euclidean(cities[i], cities[j])

# Function to calculate the total distance of the tour
def calculate_tour_cost(tour, dist_matrix):
    total_distance = 0
    max_leg_distance = 0
    for k in range(len(tour) - 1):
        dist = dist_matrix[tour[k]][tour[k+1]]
        total_distance += dist
        if dist > max_leg_distance:
            max_leg_distance = dist
    return total_distance, max_leg_distance

# Compute all permutations excluding the first city and find minimal longest leg tour
best_tour = None
min_max_leg_distance = float('inf')
best_total_distance = float('inf')

# Generate all potential tours (brute force approach, not practical for large number of cities)
for perm in permutations(range(1, num_cities)):
    current_tour = [0] + list(perm) + [0]
    total_distance, max_leg_distance = calculate_tour_cost(current_tour, dist_matrix)
    if max_leg_distance < min_max_leg_distance:
        min_max_leg_exeance = max_leg_distance
        best_tour = current_tour
        best_total_distance = total_distance

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_distance}")
print(f"Maximum distance between consecutive cities: {min_max_leg_distance}")

# Note: This brute-force approach only works for a very small set of cities. Please refer to more scalable methods (like genetic algorithms or optimization libraries) for larger city sets.