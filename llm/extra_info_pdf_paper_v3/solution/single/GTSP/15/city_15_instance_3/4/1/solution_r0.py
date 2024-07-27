import math
import itertools

# City coordinates (indices correspond to city numbers)
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Groups of cities that need exactly one visit
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(idx1, idx2):
    x1, y1 = cities[idx1]
    x2, y2 = cities[idx2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Precompute the distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Evaluate total distance for a given tour
def total_distance(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Find the shortest tour visiting one city from each group, and returning to the depot
min_total_cost = float('inf')
best_tour = None

# Iterate over all combinations of cities picking one city from each group
for combination in itertools.product(*groups):
    for permutation in itertools.permutations(combination):
        # Consider the tour from the depot
        current_tour = [0] + list(permutation) + [0]
        current_cost = total_node_distance(current_node_tour)
        
        if current_cost < min_total_cost:
            min_total_cost = current_cost
            best_tour = current_tour

# Display the results
print("Tour:", best_node_tour)
print("Total travel cost:", min_total_cost)