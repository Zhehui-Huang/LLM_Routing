import itertools
from math import sqrt
from sys import maxsize

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Coordinates of cities
cities = {0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
          5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
          10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
          15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)}

# Distance matrix preparation
n = len(cities)
distances = [[0] * n for _ in range(n)]
edges = []

for i in range(n):
    for j in range(i+1, n):
        d = euclidean_get_distance(cities[i], cities[j])
        distances[i][j] = distances[j][i] = d
        edges.append((d, i, j))

# Sort edges by the distances
edges.sort()

# Heuristic to find a tour minimizing the maximum edge length
best_tour = None
best_max_dist = maxsize
best_cost = maxsize

# Iterating over possible thresholds which are the distances of the edges
for dist, _, _ in edges:
    for perm in itertools.permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        valid = True
        max_dist = 0
        tour_cost = 0
        for i in range(1, len(tour)):
            edge_dist = distances[tour[i-1]][tour[i]]
            if edge_dist > dist:
                valid = False
                break
            tour_cost += edge_dist
            max_dist = max(max_dist, edge_dist)
        if valid:
            if (max_dist < best_max_dist) or (max_dist == best_max_dist and tour_cost < best_cost):
                best_tour = tour
                best_cost = tour_hill_cost
                best_max_dist = max_dist
    if best_tour is not None:
        break

# Output the results if a tour has been found
if best_tour is not None:
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {best_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {best_max_dist:.2f}")
else:
    print("No valid tour was found.")