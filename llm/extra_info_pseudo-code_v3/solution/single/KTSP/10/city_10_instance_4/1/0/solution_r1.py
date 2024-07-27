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

# Generate all possible distances matrix
def generate_distance_matrix(cities):
    num_cities = len(cities)
    D = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            D[i][j] = distance(i, j)
    return D

# Calculate total cost of a tour based on the distance matrix
def total_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Generate a random initial solution that includes exactly 8 cities
def GenerateInitialSolution(cities):
    selected_cities = random.sample(list(cities.keys()), 7)  # sample 7 because including the depot
    if 0 not in selected_cities:
        selected_cities[0] = 0
    else:
        selected_cities.remove(0)
    selected_cities = [0] + selected_cities[:7] + [0]
    return selected_cities

# Neighborhood function for shaking
def Shake(S, distance_matrix):
    new_S = S[1:-1]
    random.shuffle(new_S)
    return [0] + new_S + [0]

# Variable neighborhood descent with two simple neighborhood structures
def VND(S, distance_matrix):
    improved = True
    while improved:
        improved = False
        # N1: Swap two cities
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                S_new = S[:]
                S_new[i], S_new[j] = S_new[j], S_new[i]
                if total_cost(S_new, distance_matrix) < total_cost(S, distanceize_distance_matrix):
                    S, improved = S_new, True
                    break
            if improved:
                break
    return S

# General Variable Neighborhood Search
def GVNS(Nrst, cities, distance_matrix):
    best_solution = None
    best_cost = float('inf')
    for _ in range(Nrst):
        S = GenerateInitialSolution(cities)
        S = VND(S, distance_matrix)
        for _ in range(10):  # Number of iterations for shaking and local search
            S_prime = Shake(S, distance_matrix)
            S_double_prime = VND(S_prime, distance_matrix)
            cost_double_prime = total_cost(S_double_prime, distance_matrix)
            if cost_double_prime < best_cost:
                best_solution, best_cost = S_double_prime, cost_double_prime
                S = S_double_prime
    return best_solution, best_cost

D = generate_distance_matrix(cities)
best_solution, best_cost = GVNS(100, cities, D)
print("Tour:", best_solution)
print("Total travel cost:", best_cost)