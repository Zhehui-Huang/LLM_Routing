import math
import itertools
from scipy.spatial.distance import euclidean

# City coordinates
coords = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Calculate Euclidean distances between all pairs of cities
def calculate_distances(coords):
    n = len(coords)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = euclidean(coords[i], coords[j])
    return distances

# Check if all vertices are visited in the path
def is_valid_tour(path, n):
    return set(path) == set(range(n))

# Calculate the total cost and maximum leg distance of the path
def evaluate_tour(path, distances):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(path)):
        distance = distances[path[i-1]][path[i]]
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

# Generate a valid tour with heuristic approach
def generate_tour(distances):
    n = len(distances)
    min_max_distance = float('inf')
    best_tour = []

    # Testing all permutations can be infeasible for larger n, but okay for n=10
    for perm in itertools.permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        if is_valid_tour(path, n):
            total_cost, max_dist = evaluate_tour(path, distances)
            if max_dist < min_max_distance:
                min_max_distance = max_dist
                best_tour = path

    return best_tour, min_max_distance

# Main execution
distances = calculate_distances(coords)
tour, max_distance = generate_tour(distances)

# Calculate the total cost of the best tour
_, total_cost = evaluate_tour(tour, distances)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")