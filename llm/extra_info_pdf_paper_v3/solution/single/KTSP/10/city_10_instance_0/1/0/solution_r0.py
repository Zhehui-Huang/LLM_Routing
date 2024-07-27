import itertools
import math

# Cities data
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

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Selecting 3 cities to combine with the depot (0)
combinations = itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
min_cost = float('inf')
best_tour = None

for combination in combinations:
    # Including the depot city
    current_cities = [0] + list(combination)
    # Generate all permutations of these cities, starting and ending with depot
    permutations = itertools.permutations(current_cities)
    for perm in permutations:
        if perm[0] == 0 and perm[-1] != 0:
            perm = list(perm) + [0]  # Ensure tour ends at depot
            cost = calculate_tour_cost(perm)
            if cost < min_cost:
                min_cost = cost
                best_tour = perm

# Output result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")