from itertools import product
import math

# Define city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
city_groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate distances between all cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Find all combinations for cities (one from each group)
possible_tours = []
for combination in product(*city_groups):
    # Add depot to start and end
    tour = [0] + list(combination) + [0]
    possible_tours.append(tour)

# Compute the cost for each tour
min_distance = float('inf')
best_tour = None
for tour in possible_tours:
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[(tour[i], tour[i+1])]
    if total_distance < min_distance:
        min_distance = total_distance
        best_tour = tour

# Output the result
print(f'Tour: {best_tour}')
print(f'Total travel cost: {min_distance}')