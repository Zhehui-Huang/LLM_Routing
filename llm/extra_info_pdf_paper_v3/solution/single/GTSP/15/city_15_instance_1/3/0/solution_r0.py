import math
from itertools import product

# City coordinates
city_coords = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# City groups
city_groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Function to calculate Euclidean distance
def euclidean_distance(city_a, city_b):
    x1, y1 = city_coords[city_a]
    x2, y2 = city_coords[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate distance between each pair of cities
distances = {}
for i in city_coords:
    for j in city_coords:
        distances[(i, j)] = euclidean_distance(i, j)

# Find the shortest path visiting one city from each group and starting/ending at the depot
min_tour_cost = float('inf')
best_tour = []

for perm in product(*(city_groups[g] for g in city_groups)):
    # Considering all permutations of choosing one city per group
    full_tour = [0] + list(perm) + [0]
    tour_cost = sum(distances[(full_tour[i], full_tour[i+1])] for i in range(len(full_tour) - 1))
    
    if tour_cost < min_tour_cost:
        min_tour_cost = tour_cost
        best_tour = full_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_tour_cost}")