import math
import itertools
import numpy as np

# Define the cities' coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of cities
n = len(cities)

# Create a matrix of distances between each pair of cities
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = distance(i, j)

# Function to evaluate the cost of the tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        d = distance(tour[i-1], tour[i])
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

# Try all permutations, finding the one with the minimum maximum distance
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

for tour in itertools.permutations(range(1, n)):
    tour = [0] + list(tour) + [0]
    total_cost, max_distance = evaluate_tour(tour)
    if max_distance < best_max_distance:
        best_tour = tour
        best_total_cost = total_cost
        best_max_distance = max_distance

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")