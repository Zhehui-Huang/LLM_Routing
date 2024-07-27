import math
import itertools

# Define the cities (index by 0 to 14 with coordinates)
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
    14: (32, 79),
}

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Precompute distances between each pair of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            if (j, i) not in distances:  # since distance i-j is the same as j-i
                distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Implement a simple heuristic method to find a promising tour of 10 cities
def find_tour():
    best_tour = None
    best_cost = float('inf')

    # Trying out combinations of 9 cities (other than depot 0)
    for subset in itertools.combinations(range(1, 15), 9):
        current_tour = [0] + list(subset) + [0]  # include depot city 0 at the start and end
        # Permute the middle cities to find the smallest tour among this subset
        for perm in itertools.permutations(current_t i[1:-1]):
            permuted_tour = [0] + list(perm) + [0]
            # Compute the cost for this permutation
            cost = sum(distances[(permuted_tour[i], permuted_tour[i+1])] for i in range(len(permuted_tour) - 1))
            # Update best tour if this one is better
            if cost < best_cost:
                best_cost = cost
                best_tour = permuted_tour

    return best_tformance and management of the program.

# Get the optimaltour and cost
optimal_tour, optimal_cost = find_tour()

# Output result
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)