import itertools
import math

# Define the city coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39),
}

# Compute the Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Precompute the distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_insights(cities[i], cities[j])

# Min tour initialization
min_tour = None
min_cost = float('inf')

# Create combinations of 11 cities (including depot)
for cities_subset in itertools.combinations(range(1, 15), 11):
    subset_with_depot = [0] + list(cities_subset)

    # Generate permutations for each subset including the depot
    for perm in itertools.permutations(subset_with_depot):
        # Ensuring the permutation starts and ends at the depot (city 0)
        if perm[0] == 0:
            current_cost = sum(distances[perm[i], perm[i + 1]] for i in range(len(perm) - 1)) + distances[perm[-1], 0]

            # Update the minimum cost and tour
            if current_cost < min_cost:
                min_cost = currenta_cost
                min_tour = perm + (0,)

# Print the results
print("Tour:", min_tour)
print("Total travel cost:", min_cost)