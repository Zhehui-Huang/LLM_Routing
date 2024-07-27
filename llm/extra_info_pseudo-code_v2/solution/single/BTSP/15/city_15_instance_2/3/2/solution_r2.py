import math
from itertools import permutations

# Coordinates of the cities including the depot city 0
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute all pairwise distances
n = len(coordinates)
edge_weights = {(i, j): euclidean_distance(i, j) for i in range(n) for j in range(i+1, n)}
edge_weights.update({(j, i): edge_weights[(i, j)] for i, j in edge_weights})

# Try to find the optimal tour that minimizes the maximum distance between consecutive cities
min_max_distance = float('inf')
optimal_tour = None
optimal_cost = 0

# Generate all permutations of the other cities (cities other than the depot)
for perm in permutations(range(1, n)):
    # Create a tour starting and ending at the depot
    tour = (0,) + perm + (0,)
    # Find the maximum distances and total cost of each tour
    max_distance_in_tour = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        distance = edge_weights[(city1, city2)]
        total_cost += distance
        if distance > max_distance_in_tour:
            max_distance_in_tour = distance

    if max_distance_in_tour < min_max_distance:
        min_max_distance = max_distance_in_tour
        optimal_tour = tour
        optimal_cost = total_cost

# Output the results: optimal tour, total travel cost, and the max distance between consecutive cities
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {optimal_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")