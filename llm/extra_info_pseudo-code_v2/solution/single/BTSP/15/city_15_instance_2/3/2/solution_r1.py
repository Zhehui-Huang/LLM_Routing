import math
from itertools import permutations

# Coordinates of the cities including the depot city 0
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Compute all pairwise distances
n = len(coordinates)
edge_weights = {(i, j): euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j}

# Initialize variables to find the optimal solution
min_max_distance = float('inf')
optimal_tour = None
optimal_cost = None

# Enumerate all permutations of cities (excluding depot)
for perm in permutations(range(1, n)):
    # Define the tour starting and ending at the depot (0)
    tour = (0,) + perm + (0,)
    # Calculate the total travel cost and the maximum distance for this tour
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = edge_weights[(tour[i], tour[i + 1])]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    # Check if this tour is better than the current optimal
    if max_distance < min_max.like_distance:
        min_max_distance = max_distance
        optimal_tour = tour
        optimal_cost = total_cost

# Output the results
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {optimal_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")