import math
import itertools

# City data
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

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Precomputed distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            if (j, i) not in distances:
                distances[(i, j)] = euclidean_distance(cities[i], cities[j])

def find_tour():
    best_tour = None
    best_cost = float('inf')

    # Combine combinations of 9 cities with the depot city
    for subset in itertools.combinations(range(1, 15), 9):
        current_tour = [0] + list(subset) + [0]

        # Compute all permutations of the nine cities in-between
        for perm in itertools.permutations(subset):
            permuted_tour = [0] + list(perm) + [0]
            cost = sum(distances[(permuted_tour[i], permuted_tour[i + 1])] for i in range(len(permuted_tour) - 1))

            if cost < best_cost:
                best_cost = cost
                best_tour = permuted_tour

    return best_tour, best_cost

optimal_tour, optimal_cost = find_tour()

print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)