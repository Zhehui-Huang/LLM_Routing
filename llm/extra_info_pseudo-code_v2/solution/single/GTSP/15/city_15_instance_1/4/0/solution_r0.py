import math
from itertools import product

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Brute force approach to find the minimal tour (Available due to small instance size)
def find_minimal_tour():
    minimal_tour = None
    minimal_cost = float('inf')
    
    # Generate all combinations of taking one city from each group
    for combination in product(*groups):
        # Permutations of the selected cities from each group
        for permutation in itertools.permutations(combination):
            current_tour = [0] + list(permutation) + [0]  # Start and end at the depot city
            current_cost = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
            
            if current_cost < minimal_cost:
                minimal_cost = current_cost
                minimal_tour = current_tour

    return minimal_tour, minimal_cost

# Find the tour and its cost
optimal_tour, total_cost = find_minimal_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")