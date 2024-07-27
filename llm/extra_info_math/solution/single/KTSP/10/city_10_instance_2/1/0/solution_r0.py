import itertools
import math

# Provided cities with coordinates
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

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Pre-compute distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean(gradients[i], gradients[j])

# Considering all 5-city combinations including the depot city 0
min_cost = float('inf')
best_tour = None

# We choose 5 additional cities because the depot city is always included
for combo in itertools.combinations(range(1, 10), 5):
    all_cities = [0] + list(combo)  # Start and end at depot
    # Generate all permutations of chosen cities to find the shortest tour
    for perm in itertools.permutations(all_cities[1:]):
        full_tour = [0] + list(perm) + [0]  # complete cycle returning to depot
        # Calculate the total cost of this tour
        cost = sum(distances[(full_tour[i], full_tour[i+1])] for i in range(len(full_tour) - 1))
        # Update the minimum cost and tour found
        if cost < min_cost:
            min_cost = cost
            best_tour = full_tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)