import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates including the depot
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

# Calculate all pair distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Generate combinations of 5 cities excluding the depot city 0
city_indices = list(cities.keys())[1:]  # all cities excluding depot
combinations = list(itertools.combinations(city_indices, 5))

# Finding minimal distance tour
min_distance = float('inf')
best_tour = None

for combo in combinations:
    current_tour = [0] + list(combo) + [0]
    # Generate all permutations for this combination, including the depot
    permutations = itertools.permutations(current_tour[1:-1])
    for perm in permutations:
        full_tour = [0] + list(perm) + [0]
        current_distance = sum(distances[(full_tour[i], full_tour[i + 1])] for i in range(len(full_tour) - 1))
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = full_tour

# Return the best tour and the minimal tour distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")