import math
import itertools

# Given coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Number of cities
n = len(coordinates)

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Pre-calculate distances between all pairs of cities
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Find a tour that minimizes the longest edge distance
def minimize_maximum_distance():
    best_max_edge = float('inf')
    best_tour = None

    for perm in itertools.permutations(range(1, n)):
        # Create tour starting and ending at the depot (0)
        tour = [0] + list(perm) + [0]

        # Calculate maximum edge and total cost of this tour
        max_edge = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        # Update best tour found
        if max_edge < best_max_edge:
            best_max_edge = max_edge
            best_tour = tour
            best_total_cost = total_cost

    return best_tour, best_total_cost, best_max_edge

# Compute the solution
tour, total_cost, max_dist = minimize_maximum_distance()

# Display results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_dist, 2))