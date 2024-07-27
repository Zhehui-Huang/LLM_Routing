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

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix
num_cities = len(coordinates)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Calculate tour length
def tour_length(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def generate_initial_solution():
    cities = list(range(1, num_cities))  # Cities excluding the depot
    selected_cities = random.sample(cities, 3)
    initial_tour = [0] + selected_cities + [0]
    return initial_tour

def shake_solution(tour):
    # Randomly select two cities in the middle of the tour (not the first or last) to swap
    idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)
    new_tour = tour[:]
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return new_tour

def VND(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i == j:
                    continue
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if tour_length(new_tour, distance_matrix) < tour_length(tour, distance_matrix):
                    tour = new_tour
                    improved = True
    return tour

def GVNS(Nrst=100):
    best_solution = None
    best_cost = float('inf')
    for _ in range(Nrst):
        current_solution = generate_initial_solution()
        current_cost = tour_length(current_solution, distance_matrix)
        while True:
            new_solution = shake_solution(current_solution)
            new_solution = VND(new_solution)
            new_cost = tour_length(new_solution, distance_matrix)
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
            else:
            break
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    return best_solution, best_cost

# Execute the algorithm
best_tour, best_tour_cost = GVNS()

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)