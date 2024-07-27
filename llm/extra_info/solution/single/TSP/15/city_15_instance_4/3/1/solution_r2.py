import math
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Precompute distances between all pairs of cities
dist = {(i, j): distance(i, j) for i in cities for j in cities if i != j}

# Held-Karp algorithm
def held_karp():
    # Memory for storing solutions to subproblems
    C = {}

    # Initial step: base cases with two nodes
    for k in cities:
        if k == 0: continue
        C[(frozenset([0, k]), k)] = (dist[0, k], [0, k])

    # Dynamic programming:
    for subset_size in range(3, len(cities) + 1):
        for subset in combinations([c for c in cities if c != 0], subset_size - 1):
            subset = frozenset(subset).union({0})
            for k in subset - {0}:
                C[(subset, k)] = min((C[(subset - {k}, m)][0] + dist[m, k], C[(subset - {k}, m)][1] + [k]) for m in subset if m != k)

    # Adding return to the starting city
    all_nodes = frozenset(cities)
    result = min((C[(all_nodes, m)][0] + dist[m, 0], C[(all_nodes, m)][1] + [0]) for m in cities if m != 0)

    return result

tour, total_cost = held_karp()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")