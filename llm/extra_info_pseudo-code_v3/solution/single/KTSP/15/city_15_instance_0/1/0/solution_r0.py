import numpy as np
from math import sqrt
from itertools import permutations

# Define the cities with their coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create the distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Function to calculate the total tour cost
def tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Generate all possible tours starting and ending at 0 and visiting exactly 3 other cities
def all_possible_tours():
    other_cities = list(range(1, n))
    for cities_tour in permutations(other_cities, 3):
        yield [0] + list(cities_tour) + [0]

# Find the minimum cost tour using the brute-force algorithm
def find_minimum_tour():
    best_tour = None
    best_cost = float('inf')
    for tour in all_possible_tours():
        cost = tour_cost(tour, distance_matrix)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour, best_cost

# Execution
min_tour, min_cost = find_minimum_tour()
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost}")