import math

# Define the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
dist_matrix = {}
for i in cities:
    dist_matrix[i] = {}
    for j in cities:
        dist_matrix[i][j] = calculate_distance(cities[i], cities[j])

# Initialize variables to keep track of the best tour
best_tour = None
min_max_distance = float('inf')

# Brute-force way to find minimum longest leg (limited because using permutations for larger number of cities becomes infeasible)
from itertools import permutations

def evaluate_tour(tour):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = dist_matrix[tour[i]][tour[i + 1]]
        total_distance += distance
        max_distance = max(max_distance, distance)
    return total_distance, max_distance

# Generate all permutations of city visits not including the depot
for perm in permutations(range(1, 10)):
    tour = [0] + list(perm) + [0]
    total_distance, max_distance = evaluate_tour(tour)
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_total_distance = total_distance

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_distance}")
print(f"Maximum distance between consecutive cities: {min_max_distance}")