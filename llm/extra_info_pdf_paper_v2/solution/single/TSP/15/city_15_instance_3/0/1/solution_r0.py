import numpy as np
import math
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73), 6: (6, 61),
    7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate the euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Dictionary to store the distances
distances = {(i, j): euclidean or math.inf for i in cities for j in cities if i != j}

# Calculating distances between every pair of cities
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Implementing a simple function to calculate the trip length
def calculate_tour_length(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# We start with a naive solution: visiting cities in numerical order and returning to the depot
initial_tour = list(cities.keys()) + [0]
initial_cost = calculate_tour_length(initial_tour)

def find_best_tour():
    best_tour = initial_tour
    best_cost = initial_cost
    
    # Generate permutations for all cities except the depot
    for perm in permutations(list(cities.keys())[1:]):
        current_tour = [0] + list(perm) + [0]
        current_cost = calculate_tour_length(current_tour)
        
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost

    return best_tour, best_cost

# Finding the best tour using permutation (feasible for small number of cities)
best_tour, best_cost = find_best_tour()

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", best_cost)