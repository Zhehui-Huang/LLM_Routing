from itertools import permutations
import math

# Define the coordinates of each city including the depot
cities = {
    0: (8, 11),   1: (40, 6),    2: (95, 33),  3: (80, 60),  4: (25, 18),
    5: (67, 23),  6: (97, 32),   7: (25, 71),  8: (61, 16),  9: (27, 91),
    10: (91, 46), 11: (40, 87),  12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43),  17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Compute the distance matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean distance(cities[i], cities[j])

# Variable to hold the best path and respective paths and distances
min_max_distance = float('inf')
min_total_cost = float('inf')
best_tour = None

# Test all permutations of the cities (except city 0)
for perm in permutations(range(1, n)):
    # Start and end at depot city 0
    tour = [0] + list(perm) + [0]
    
    # Calculate total tour cost and max distance
    total_cost = 0
    max_dist = 0
    
    for i in range(len(tour) - 1):
        dist = distance_matrix[tour[i]][tour[i+1]]
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    
    # Check if this ordering improves the optimal solution
    if max_dist < min_max_distance or (max_dist == min_max_dist and total_cost < min_total_cost):
        min_max_distance = max_dist
        min_total_cost = total_cost
        best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)