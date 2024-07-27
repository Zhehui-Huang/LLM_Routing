import numpy as np
from itertools import permutations
from random import randint, sample
import math

# Helper functions
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Initialization of cities and distance matrix
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Generate initial solution
def generate_initial_solution():
    tour = [0] + sample(list(cities.keys())[1:], 5)
    tour.append(0)
    return tour

# Shake function
def shake(solution):
    middle_section = solution[1:-1]
    np.random.shuffle(middle_section)
    return [0] + middle_section + [0]

# Variable Neighborhood Descent
def vnd(solution):
    improved = True
    while improved:
        improved = False
        best_cost = calculate_tour_cost(solution, distance_matrix)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if j - i == 1: continue  # adjacent swap does nothing
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_tour_cost(new_solution, distance_matrix)
                if new_cost < best_cost:
                    solution = new_solution
                    best_cost = new_cost
                    improved = True
    return solution

# GVNS main
def gvns(k_max=5, nrst=10):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        current_solution = generate_initial_solution()
        current_cost = calculate_tour_cost(current_solution, distance_matrix)
        
        for _ in range(k_max):
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_cost = calculate_tour_cost(new_solution, distance_matrix)
            
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Run the GVNS algorithm
best_tour, best_tour_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)