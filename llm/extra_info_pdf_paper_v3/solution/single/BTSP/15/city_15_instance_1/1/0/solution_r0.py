import math
from scipy.spatial import distance_matrix
from itertools import permutations

# City coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
          (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
          (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Calculate distance matrix
distances = distance_matrix(cities, cities)

# Function to compute the total travel cost and maximum distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = distances[tour[i-1], tour[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    # Return to the depot
    return_dist = distances[tour[-1], tour[0]]
    total_cost += return_dist
    if return_dist > max_distance:
        max_distance = return_dist
    return total_cost, max_distance

# Find the optimal tour by checking all permutations (Brute-force for demonstration)
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

for perm in permutations(range(1, len(cities))):
    current_tour = [0] + list(perm) + [0]
    total_cost, max_dist = evaluate_tour(current_tour)
    if max_dist < best_max_distance:
        best_max_distance = max_dist
        best_tour = current_tour
        best_total_cost = total_cost

# Output the best solution found
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_amount}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")