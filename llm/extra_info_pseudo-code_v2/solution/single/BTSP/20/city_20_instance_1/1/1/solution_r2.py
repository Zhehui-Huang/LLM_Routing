import numpy as np
from itertools import permutations

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Calculate Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Compute matrix of distances between each city
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Brute force approach to find the optimal tour minimizing the longest leg
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    all_tours = permutations(range(1, n))  # Generate permutations of all cities except the depot

    for tour in all_tours:
        full_tour = [0] + list(tour) + [0]
        max_leg_distance = max(distances[full_tour[i]][full_tour[i+1]] for i in range(len(full_tour) - 1))
        
        if max_leg_distance < min_max_distance:
            min_max_distance = max_leg_distance
            best_tour = full_tour

    # Compute total cost of the tour
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

    return best_tour, total_cost, min_max_distance

# Find and print the optimal tour
optimal_tour, total_travel_cost, max_travel_distance = find_optimal_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_travel_distance:.2f}")