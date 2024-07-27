import itertools
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Compute all pairwise city distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(*cities[i], *cities[j])

# Generate all combinations of 3 additional cities to visit besides the depot
city_combinations = itertools.combinations(range(1, 10), 3)

min_cost = float('inf')
best_tour = None

# Evaluate all permutations of each combination to find the minimum cost tour
for combo in city_combinations:
    for perm in itertools.permutations(combo):
        # Create a tour starting and ending at city 0
        tour = [0] + list(perm) + [0]
        cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Display the result
print(f"Tour: {best_tour}")
print(f"Total travel and candidates: {min_cost:.2f}")