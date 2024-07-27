import itertools
import math

# Define a function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p2[1] - p1[1])**2)

# List of city coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate distances matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Define function to find the minimum tour that includes exactly 13 cities
def find_min_tour():
    min_cost = float('inf')
    best_tour = []

    all_combinations = itertools.combinations(range(1, n), 12)  # Combinations of 12 cities (excluding the depot)
    for comb in all_combinations:
        current_cities = [0] + list(comb)  # Always include depot city 0

        # Generate all permutations of the selected cities
        for perm in itertools.permutations(current_cities[1:]):
            tour = [0] + list(perm) + [0]  # Create a tour starting and ending at the depot

            # Calculate the cost of the tour
            cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

            # Update the best tour if a new minimum cost is found
            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tour, min_cost

# Solve the problem
optimal_tour, total_cost = find_min_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))