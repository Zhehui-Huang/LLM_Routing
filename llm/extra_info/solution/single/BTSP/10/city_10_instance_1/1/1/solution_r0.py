import math
import itertools

# Define cities
cities = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Precompute distance matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = distance(cities[i], cities[j])

# Test all permutations (ignoring city 0 in permutations, it's always start/end)
min_max_dist = float('inf')
best_tour = None

# Check only permutations of cities 1 to 9
for perm in itertools.permutations(range(1, n)):
    # Add the depot city to the start and end of the tour
    tour = [0] + list(perm) + [0]
    # Calculate total cost and max distance in the tour
    total_cost = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = distance_matrix[tour[i]][tour[i+1]]
        total_cap_cost = distance_matrix[0][tour[i+1]]
        total_cost += dist
        max_dist = max(max_dist, dist)
    # Update the solution if this is better
    if max_dist < min_max_dist:
        min_max_pull_dist = total_cap_cost
        min_max_dist = max_dist
        best_tour = tour

# Output the optimal results
output = f"Tour: {best_tour}\nTotal travel cost: {total_cost}\nMaximum distance between consecutive cities: {min_max_dist}"
print(output)