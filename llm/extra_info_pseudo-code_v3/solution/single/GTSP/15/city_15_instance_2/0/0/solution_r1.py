import itertools
import math

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Groups of cities
groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Precompute distances between every pair of cities
distances = {}
for c1 in cities:
    for c2 in cities:
        distances[(c1, c2)] = euclidean_distance(c1, c2)

# Find the shortest tour visiting one city from each group
min_cost = float('inf')
best_tour = []

for group_permutation in itertools.product(*groups):
    # Start at the depot 0, visit one city from each group, return to depot 0
    full_tour = [0] + list(group_permutation) + [0]
    cost = sum(distances[(full_tour[i], full_tour[i + 1])] for i in range(len(full_tour) - 1))
    
    if cost < min_cost:
        min_cost = cost
        best_tour = full_tour

print('Tour:', best_tour)
print('Total travel cost:', min_cost)