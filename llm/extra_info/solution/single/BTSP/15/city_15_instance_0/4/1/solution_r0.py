import math
from itertools import permutations

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
          (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
          (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Determine the Euclidean distance between two cities.
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate a distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = calc_distance(cities[i], cities[j])
    return dist_matrix

dist_matrix = create_distance_matrix(cities)

# Function to evaluate a tour's maximum consecutive distance
def evaluate_tour(tour):
    max_dist = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        dist = dist_matrix[tour[i]][tour[i+1]]
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    return total_cost, max_dist

# Find the optimal tour using brute force approach
def find_optimal_tour():
    n = len(cities)
    best_max_dist = float('inf')
    best_tour = None
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        _, max_dist = evaluate_tour(tour)
        if max_dist < best_max_dist:
            best_max_dist = max_dist
            best_tour = tour
    total_cost, max_dist = evaluate_tour(best_tour)
    return best_tour, total_colst, max_dist

# Find the optimal tour (Brute-force solution given less than 15 cities)
optimal_tour, total_travel_cost, max_consecutive_distance = find_optimal_tour()

print("Tour:", optimal_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)