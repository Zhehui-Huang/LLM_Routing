import math
import itertools

# Coordinates of the depot and cities
locs = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88),
    (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
n = len(locs)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(locs[i], locs[j])

# Try all permutations of the cities (except the depot which is fixed at start and end)
min_tour = None
min_cost = float('inf')

# Generate all cities indices except the depot 0
cities = list(range(1, n))

for tour in itertools.permutations(cities):
    # Calculate the cost of the tour starting and ending at the depot
    cost = distance_matrix[0][tour[0]]  # start from the depot to the first city
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1]][tour[i]]  # sum costs between consecutive cities in the tour
    cost += distance_matrix[tour[-1]][0]  # cost from last city back to the depot

    # Compare to find the minimum cost tour
    if cost < min_cost:
        min_cost = cost
        min_tour = tour

# Format the tour to start and end at the depot 0
optimised_tour = [0] + list(min_tour) + [0]

# Print the optimized tour and cost
print("Tour:", optimised_tour)
print("Total travel cost:", min_cost)