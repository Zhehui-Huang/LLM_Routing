import math
import random

# Problem Data
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
    9: (66, 62),
}

group_indices = [
    [1, 4],  # Group 0
    [2, 6],  # Group 1
    [7],     # Group 2
    [5],     # Group 3
    [9],     # Group 4
    [8],     # Group 5
    [3],     # Group 6
]

# Distance Calculation Function
def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points (tuples)."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Precompute all distances between all cities
distances = {}
for i in cities.keys():
    for j in cities.keys():
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Heuristic Method to Solve the MGSP
def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Let's check all permutations of choosing one city from each group
    from itertools import product
    for combination in product(*group_indices):
        current_tour = [0] + list(combination) + [0]
        current_cost = sum(distances[(current_tour[i], current_tour[i + 1])] for i in range(len(current_tour) - 1))

        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
            
    return best_tour, best_cost

# Finding the optimal route
tour, total_cost = find_shortest_tour()

# Output the results as specified
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")