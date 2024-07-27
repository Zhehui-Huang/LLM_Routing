import math
import random

# Coordinates for the depot and the cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), 
    (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

# Define function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Distance matrix calculation
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Generate subsets of cities including the depot
def generate_subsets(cities, include_depot=True):
    from itertools import combinations
    depot = [0]
    other_cities = list(range(1, n))
    k = 9  # We need 9 other cities because the depot is always included
    select_combinations = [depot + list(comb) for comb in combinations(other_cities, k)]
    return select_combinations

# Function to calculate the total distance of a tour
def calculate_tour_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Randomly iterate over generated subsets, finding and returning the shortest tour
def find_shortest_tour():
    subsets = generate_subsets(range(1, n))
    best_tour = None
    best_cost = float('inf')
    for subset in subsets:
        for perm in permutations(subset):
            current_tour = [0] + list(perm) + [0]
            current_cost = calculate_tour_distance(current_tour)
            if current_cost < best_cost:
                best_tour = current_tour
                best_cost = current_cost
    return best_tour, best_cost

# Finding the shortest possible tour
best_tour, best_cost = find_shortest_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)