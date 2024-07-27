import itertools
import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        if i not in distance_matrix:
            distance_matrix[i] = {}
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Choose 5 cities (excluding the depot)
city_combinations = itertools.combinations(range(1, 10), 5)
min_tour_cost = float('inf')
optimal_tour = []

# Explore all combinations and permutations for shortest tour
for comb in city_combinations:
    full_comb = [0] + list(comb)  # Include depot
    permutations = itertools.permutations(full_comb)
    for perm in permutations:
        # Ensure the tour starts and ends at depot, city 0
        if perm[0] == 0 and perm[-1] == 0:
            continue
        tour = list(perm) + [0]  # Close the tour back at the depot
        # Calculate the total cost of this permutation
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += distance_matrix[tour[i]][tour[i + 1]]

        # Check if this tour is better than the previous minimum
        if total_cost < min_tour_cost:
            min_tour_cost = total_cost
            optimal_tour = tour

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", min_tour_cost)