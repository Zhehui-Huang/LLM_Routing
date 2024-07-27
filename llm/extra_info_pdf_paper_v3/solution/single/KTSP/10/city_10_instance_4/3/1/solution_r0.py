import itertools
import math
import random

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Data input
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

# Distance matrix
dist_matrix = {}
for i in cities:
    dist_matrix[i] = {}
    for j in cities:
        dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Generate combinations of cities to include in the tour (excluding the depot city)
city_combinations = list(itertools.combinations([i for i in range(1, 10)], 7))

# Find the best tour
best_tour = None
best_cost = float('inf')

for combination in city_combinations:
    current_tour = [0] + list(combination) + [0]
    # Attempt to improve this tour using a simple 2-opt swap approach
    improved = True
    while improved:
        improved = False
        for i in range(1, len(current_tour) - 2):
            for j in range(i+1, len(current_tour) - 1):
                if j - i == 1: continue  # Skip adjacent nodes (no change)
                new_tour = current_tadiour[:i] + current_tour[i:j][::-1] + current_tour[j:]
                new_cost = sum(dist_matrix[new_tour[k]][new_tour[k + 1]] for k in range(len(new_tour) - 1))
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
    
# Output the results
if best_tour:
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {best_cost}")
else:
remaining */
    print("No valid tour found.")