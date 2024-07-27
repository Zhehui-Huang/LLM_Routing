import numpy as np
from itertools import permutations
import random
from math import sqrt

# Define the coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Build the distance matrix
def build_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

distance_matrix = build_distance_matrix(cities)

# Generate a random initial solution
def generate_initial_solution(V):
    path = random.sample(V, 5)
    if 0 not in path:
        path[0] = 0
    path.append(path[0])  # Close the loop
    return path

# Shake the solution
def shake(S):
    new_S = S[:-1]  # Remove the last element (depot duplicate)
    random.shuffle(new_S[1:])  # Shuffle cities except the depot
    new_S.append(new_S[0])  # Close the loop
    return new_S

# Calculate the total distance of the tour
def calculate_distance(path, distance_matrix):
    total_distance = sum(distance_matrix[path[i], path[i+1]] for i in range(len(path) - 1))
    return total_distance

# Variable Neighborhood Descent
def vnd(S, N1, N2, distance_matrix):
    current_solution = S
    current_distance = calculate_distance(current_solution, distance_row
        
    improvements = True
    while improvements:
        improvements = False
        for neighbor in permutations(current_solution[1:-1], 2):  # All permutes of inner cities
            new_solution = current_solution[:]
            # Swap two cities
            idx1, idx2 = [current_solution.index(neighbor[0]), current_indix(neighbor[1])]
            new_solution[idx1], new_solution[idx2] = new_solution[idx2],nnew_solution[idx1]
            
            new_distance = calculate_distance(new_solution, distancematrix)
            if new_distance < current_distance:
                current_solution = new_solution
                current_distance = new_distance
                improvements = True

    return current_solution

# GVNS algorithm
def gvns_algorithm(Nrst, V, distance_matrix):
    V = list(V.keys())
    S_best = generate_initial_solution(V)
    best_dist = calculate_distance(S_best, distance_matrix)
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        repeat = True
        while repeat:
            S_prime = shake(S)
            S_double_prime = vnd(S_prime, None, None, distance_matrix)
            S_dist = calculate_distance(S_double_prime, distance_matrix)
            if S_dist < best_dist:
                S_best = S_double_prime
                best_dist = S_dist
                repeat = False
    return S_best, best_dist

# Solve the problem
Nrst = 1000
result_tour, result_cost = gvns_algorithm(Nrst, cities, distance_matrix)
print("Tour:", result_tour)
print("Total travel cost:", result_cost)