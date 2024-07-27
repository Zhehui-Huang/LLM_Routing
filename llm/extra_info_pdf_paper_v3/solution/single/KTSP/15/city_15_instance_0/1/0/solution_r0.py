import math
from itertools import permutations

# City coordinates
cities = {
    0: (9, 93),   1: (8, 51),   2: (74, 99),  3: (78, 50),
    4: (21, 23),  5: (88, 59),  6: (79, 77),  7: (63, 23),
    8: (19, 76),  9: (21, 38),  10: (19, 65), 11: (11, 40),
    12: (3, 21),  13: (60, 55), 14: (4, 39)
}

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Precompute distances
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Find the shortest tour that visits 4 cities including the depot city
min_cost = float('inf')
best_tour = None

# Generate all combinations of 3 additional cities
for combination in permutations(range(1, n), 3):
    current_tour = [0] + list(combination) + [0]
    current_cost = sum(distance_matrix[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
    
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")