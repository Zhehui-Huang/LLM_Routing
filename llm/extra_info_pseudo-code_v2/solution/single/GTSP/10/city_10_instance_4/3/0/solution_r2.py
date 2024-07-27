import math
from itertools import permutations

# Helper function to calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# City coordinates
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

# Grouping of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Precompute distances between all cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate_distance(cities[i], cities[j])

# Explore all permutations of one city from each group; find the minimal cost tour
minimal_tour = None
minimal_cost = float('inf')

# Generate all combinations of choosing one city per group
for combination in permutations([0] + [grp[0] for grp in groups]):
    # Check all permutations of these choices
    for perm in permutations(combination):
        if perm[0] == 0 and perm[-1] == 0:  # Ensure tour starts and ends at the depot
            cost = sum(distances[(perm[i], perm[i+1])] for i in range(len(perm)-1))
            if cost < minimal_cost:
                minimal_cost = cost
                minimal_tour = perm

# Output the results
print("Tour:", minimal_tour)
print("Total travel cost:", minimal_cost)