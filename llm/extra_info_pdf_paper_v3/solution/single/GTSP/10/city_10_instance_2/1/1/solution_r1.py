import itertools
import math

# Coordinates of the cities
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

# City groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Euclidean distance calculation
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate all permutations of one city per group
group_permutations = list(itertools.product(*groups.values()))

# Find best tour considering each permutation of groups
best_tour = None
best_distance = float('inf')

for permutation in group_permutations:
    # Include the depot city as the start and end of the tour
    tour = [0] + list(permutation) + [0]
    tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    if tour_distance < best_distance:
        best_tour = tour
        best_distance = tour_distance # Corrected the variable assignment here

# Output the best tour and the distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance}")