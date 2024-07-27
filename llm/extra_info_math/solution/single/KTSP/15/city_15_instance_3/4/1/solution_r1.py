import random
import math
from itertools import permutations

# Coordinates of cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Distance calculation using Euclidean formula
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Construct pairwise distance matrix
n = len(coordinates)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Calculate the total cost of the tour
def calculate_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Perform the 2-opt optimization algorithm
def two_opt(tour, distances):
    improved = True
    while improved:
        improved = False
        best_cost = calculate_cost(tour, distances)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                new_tour = tour[:]
                new_tour[i:j] = tour[i:j][::-1]
                new_cost = calculate_cost(new_tour, distances)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
    return tour, best_cost

# Heuristic to find a good tour
def find_best_tour(distances):
    min_tour = None
    min_cost = float('inf')
    
    # Generating all subsets of cities that include the depot and have exactly 10 cities
    cities_to_choose = list(range(1, 15))  # Cities without the depot
    for cities in combinations(cities_to_choose, 9):  # Choose 9 other cities besides the depot
        tour = [0] + list(cities) + [0]  # Start and end at the depot
        tour, cost = two_opt(tour, distances)
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    
    return min_tour, min_cost

# Look for the best tour
best_tour, best_cost = find_best_tour(distances)

# Print results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)