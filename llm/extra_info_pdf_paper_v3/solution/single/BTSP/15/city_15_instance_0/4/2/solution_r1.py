import math
import itertools

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(c1, c2):
    """Computes Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate pairwise distances
distances = [[0] * 15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Generate all possible tours that start and end at city 0
all_tours = itertools.permutations(range(1, 15))

# Evaluate each possible tour and track the minimal maximum edge
best_tour = None
best_max_edge = float('inf')
best_total_distance = float('inf')

for tour in all_tours:
    # Include starting at city 0 and returning to city 0
    full_tour = [0] + list(tour) + [0]
    max_edge = 0
    total_distance = 0
    for i in range(len(full_tour) - 1):
        edge_length = distances[full_tour[i]][full_tour[i + 1]]
        max_edge = max(max_edge, edge_length)
        total_distance += edge_length
    if max_edge < best_max_edge or (max_edge == best_max_edge and total_distance < best_total_distance):
        best_tour = full_tour
        best_max_edge = max_edge
        best_total_distance = total_distance

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_total_distance)
print("Maximum distance between consecutive cities:", best_max_edge)