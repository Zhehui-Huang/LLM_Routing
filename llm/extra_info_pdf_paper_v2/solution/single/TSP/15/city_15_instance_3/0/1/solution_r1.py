import numpy as np
import math
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73), 6: (6, 61),
    7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Dictionary to store the distances
distances = {(i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j}

# Function to calculate the tour length
def calculate_tour_length(tour):
    length = 0
    for i in range(len(tour) - 1):
        length += distances[(tour[i], tour[i+1])]
    return length

# Find the best tour by checking permutations of cities (excluding the depot city)
def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    
    for perm in permutations(list(cities.keys())[1:]):
        # Create full tour by adding the depot at the start and end
        tour = [0] + list(perm) + [0]
        cost = calculate_tour_length(tour)
        
        if cost < best_cost:
            best_tour = tour
            best_cost = cost

    return best_tour, best_cost

# Finding the best tour
best_tour, best_cost = find_best_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)