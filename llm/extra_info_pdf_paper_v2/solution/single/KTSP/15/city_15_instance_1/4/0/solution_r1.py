import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

def find_best_tour(distance_matrix, k):
    n = len(distance_matrix)
    best_tour = None
    best_cost = float('inf')
    
    for comb in permutations(range(1, n), k - 1):
        tour = [0] + list(comb) + [0]
        cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if cost < best_cost:
            best_cost = cost
            best_tour = tour

    return best_tour, best_cost

# Coordinates of the cities
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Generate the distance matrix
distance_matrix = calculate_distance_matrix(cities)

# Number of cities robot has to visit, including the depot
k = 6

# Find the best tour and its cost
best_tour, best_cost = find_best_tour(distance_matrix, k)

# Print result
print("Tour:", best_tour)
print("Total travel cost:", best_cost)