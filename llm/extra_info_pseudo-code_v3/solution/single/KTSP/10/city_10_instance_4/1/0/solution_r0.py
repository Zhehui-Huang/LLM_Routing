import numpy as np
import random
import math

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible distances
def generate_distance_matrix(cities):
    num_cities = len(cities)
    D = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            D[i][j] = distance(i, j)
    return D

def total_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Variable Neighborhood Descent (VND) implementation
def VND(S, N1, N2, distance_matrix):
    improved = True
    while improved:
        improved = False
        for neighbor in N1(S):
            if total_cost(neighbor, distance_matrix) < total_tour_cost:
                S = neighbor
                improved = True
                break
        if not improved:
            for neighbor in N2(S):
                if total_cost(neighbor, distance_matrix) < total_tour_cost:
                    S = neighbor
                    improved = True
                    break
    return S

# Generate a random initial solution
def GenerateInitialSolution(cities):
    selected_cities = random.sample(list(cities.keys()), 8)
    if 0 not in selected_cities:
        selected_cities[0] = 0
    return [0] + selected_cities[1:] + [0]

# Neighbors generator for the Shake function
def Shake(S, k):
    new_S = S[1:-1]
    random.shuffle(new_S)
    return [0] + new_shot[:k-2] + [0]

# GVNS algorithm implementation
def GVNS(Nrst, cities, distance_matrix):
    best_solution = None
    best_cost = float('inf')
    for _ in range(Nrst):
        S = GenerateInitialServiceList(cities)
        while True:
            S_prime = Shake(S, 8)
            S_double_prime = VND(S_prime, lambda s: [s], lambda s: [s], distance_matrix)
            current_cost = total_cost(S_double_prime, distance_matrix)
            if current_cost < best_cost:
                 best_solution = S_double_prime
                 best_cost = current_cost
            else:
                break
    return best_solution, best_cost

# Setting up the problem and solving it
D = generate_distance_matrix(cities)
best_solution, best_cost = GVNS(100, cities, D)
print("Tour:", best_solution)
print("Total travel cost:", best_cost)