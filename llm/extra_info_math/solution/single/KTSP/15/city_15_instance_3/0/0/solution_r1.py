import itertools
import math

# Given cities with coordinates including depot (city 0)
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92),
    (54, 93), (34, 73), (6, 61), (86, 69),
    (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]

# Function to calculate euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create distance matrix
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Function to find the shortest tour
def find_shortest_tour():
    min_tour_length = float('inf')
    best_tour = []

    # Generate combinations of cities to visit excluding depot city (index zero)
    subsets = itertools.combinations(range(1, n), 9)  # choose 9 cities since one is the depot

    for subset in subsets:
        # Include depot at the start and the end
        full_tour = [0] + list(subset) + [0]

        # Generate permutations of the selected cities, excluding the first and last position (depot)
        for permuted_subset in itertools.permutations(subset):
            current_tour = [0] + list(permuted_subset) + [0]
            current_tour_length = sum(distance_matrix[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))

            # Store the shortest tour
            if current_tour_length < min_tour_length:
                min_tour_length = current_tour_length
                best_tour = current_tour

    return best_tour, min_tour_length

# Execute function to find the best tour and its corresponding total distance
tour, total_cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)