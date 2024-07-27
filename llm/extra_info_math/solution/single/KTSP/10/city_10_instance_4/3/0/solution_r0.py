import numpy as np
import itertools

# Defining coordinates for the cities
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

# Calculate distance matrix using Euclidean distance
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distance_matrix = {}
for i in cities:
    for j in cities:
        if i not in distance_matrix:
            distance_matrix[i] = {}
        distance_matrix[i][j] = calculate_distance(cities[i], cities[j])

# Find a suitable tour starting and ending at depot with exactly 8 cities visited
def find_tour():
    # Generate all combinations of 8 cities including the depot city
    all_combinations = itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8)
    best_tour = None
    best_cost = float('inf')
    
    for combination in all_combinations:
        if 0 not in combination:
            continue
        # Generate all permutations of the selected 8 cities starting and ending at the depot
        for perm in itertools.permutations(combination):
            if perm[0] != 0 or perm[-1] != 0:
                continue
            # Calculate total cost of this permutation
            cost = sum(distance_matrix[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
            if cost < best_cost:
                best_cost = cost
                best_tour = list(perm)
    
    return best_tour, best_cost

tour, total_cost = find_tour()

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)