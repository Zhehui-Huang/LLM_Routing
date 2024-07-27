import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cities data
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate distances matrix
dist_matrix = [[0] * 15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Choosing 9 additional cities (1-indexed for easier combinations) and finding route
def find_min_tour():
    import random
    from copy import deepcopy

    def total_distance(tour):
        return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    # Randomly choose detour cities and perform local search for a best solution
    best_tour = None
    best_cost = float('inf')

    ## Generate many initial random tours and use iterative improvement
    attempts = 10000
    for _ in range(attempts):
        cities_indices = random.sample(range(1, 15), 9)
        cities_indices = [0] + cities_indices + [0]
        random.shuffle(cities_indices[1:-1])  # shuffle intermediary cities

        # Improvement: iterated local swaps
        improved = True
        while improved:
            improved = False
            for i in range(1, len(cities_indices)-2):
                for j in range(i+2, len(cities_indices)):
                    new_tour = deepcopy(cities_indices)
                    new_tour[i:j] = reversed(cities_indices[i:j])
                    if total_distance(new_tour) < total_distance(cities_indices):
                        cities_indices = new_tour
                        improved = True

        current_cost = total_distance(cities_indices)
        if current_cost < best_cost:
            best_tour = cities_indices
            best_cost = current_cost
    
    return best_tour, best_cost

final_tour, total_cost = find_min_tour()
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost: .2f}")