import numpy as np
import itertools
import random
from math import sqrt

# City coordinates
coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98),
    (51, 69), (47, 39), (62, 26), (79, 31),
    (61, 90), (42, 49)
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix
num_cities = len(coordinates)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Function to calculate tour length
def tour_length(tour):
    length = 0
    for i in range(len(tour) - 1):
        length += distance_matrix[tour[i]][tour[i+1]]
    return length

# Generate an initial random solution of 4 cities starting and ending at the depot
def generate_initial_solution():
    cities = list(range(1, num_cities))  # Exclude the depot city
    selected_cities = random.sample(cities, 3)
    tour = [0] + selected_cities + [0]
    return tour

# Shaking procedure: randomly swap two non-depot cities in the tour
def shake(tour):
    new_tour = tour[:]
    idx1, idx2 = random.sample(range(1, len(tour)-1), 2)
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return new_tour

# Variable Neighborhood Descent to improve the shaken tour
def VND(tour):
    best_tour = tour[:]
    best_length = tour_length(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_length = tour_length(new_tour)
                if new_length < best_length:
                    best_length = new_length
                    best_tour = new_tour
                    improved = True
    return best_tour

# General Variable Neighborhood Search
def GVNS(iterations):
    best_solution = generate_initial_solution()
    best_cost = tour_length(best_solution)
    for _ in range(iterations):
        current_solution = shake(best_solution)
        new_solution = VND(current_solution)
        new_cost = tour_length(new_solution)
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost
    return best_solution, best_cost

# Main execution
best_tour, best_cost = GVNS(100)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))