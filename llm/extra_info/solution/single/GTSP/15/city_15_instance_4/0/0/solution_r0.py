import itertools
import math

# Coordinates of cities, including depot
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Groups of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14],
    [5, 9], [7, 12], [10, 11]
]

# Calculate distances
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Precompute distances between all pairs
n = len(coordinates)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = distance(coordinates[i], coordinates[j])

# Function to compute total travel cost of a tour
def total_cost(tour):
    total = 0
    for k in range(1, len(tour)):
        total += distances[tour[k-1]][tour[k]]
    return total

# Compute shortest tour going through one city from each group and returning to the depot
best_tour = None
min_cost = float('inf')

# Iterate through all combinations of selecting one city from each group
for selected_cities in itertools.product(*groups):
    selected_cities = [0] + list(selected_cities) + [0]
    # Permute the selected cities (excluding the depot repeats) to find the minimum tour cost
    for permuted_cities in itertools.permutations(selected_cities[1:-1]):
        tour = [0] + list(permuted_cities) + [0]
        cost = total_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Print the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")