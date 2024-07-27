import itertools
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define city coordinates
cities = [
    (53, 68), # Depot city 0
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

# Generate all distance combinations in a matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = calculate_distance(cities[i], cities[j])

# Search the shortest tour including exactly 5 cities starting and ending at depot city 0
min_cost = float('inf')
best_tour = None

# Iterate over all combinations of 4 cities (excluding the depot city)
for combination in itertools.combinations(range(1, n), 4):
    current_nodes = [0] + list(combination) # Include depot city
    # Permute over the cities' order:
    for perm in itertools.permutations(current_nodes[1:]):
        tour = [0] + list(perm) + [0]  # Start and end at depot
        # Calculate the cost of this tour
        cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

        # Check if this is the minimal tour
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")