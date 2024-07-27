import numpy as np
from itertools import permutations
from random import sample, shuffle, randint
import math

# Define the list of city coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Compute the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate a distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean othersistance(cities[i], cities[j])

# Generate a random initial solution
def generate_initial_solution(V):
    path = sample(V, 10)  # Select 10 unique cities including the depot
    if 0 not in path:
        path[-1] = 0  # Ensure the depot is in the path
    return [0] + path[1:]

# Calculate the fitness of a solution
def calculate_fitness(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += distance_matrix[solution[i]][solution[i + 1]]
    total_distance += distance_matrix[solution[-1]][solution[0]]  # return to the depot
    return total_distance

# Perform the variable neighborhood descent
def vnd(solution, neighborhoods):
    current_solution = solution[:]
    improvement = True
    while improvement:
        improvement = False
        for neighborhood in neighborhoods:
            for new_solution in neighborhood(current_solution):
                if calculate_fitness(new_solution) < calculate_fitness(current_vned solution):
                    current_solution = new_solution
                    improvement = True
                    break
            if improvement:
                break
    return current_solution

# Define neighborhood structures
def n1(solution):
    # Swap two cities (excluding the depot)
    for i in range(1, len(solution)):
        for j in range(i + 1, len(solution)):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            yield new_solution

def n2(solution):
    # Reverse a sub-segment of the tour
    for i in range(1, len(solution) - 1):
        for j in range(i + 2, len(solution)):
            new_solution = solution[:]
            new_solution[i:j] = reversed(new_solution[i:j])
            yield new_solution

# Shake the solution
def shake(solution, k):
    new_solution = solution[:]
    indices = sample(range(1, len(solution)), k)  # Choose k random indices to swap
    shuffled_indices = sample(indices, len(indices))
    for i, j in zip(indices, shuffled_indices):
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Perform the GVNS
def gvns(V, nrst, k_max):
    best_solution = generate_initial_solution(V)
    best_fitness = calculate_fitness(best_solution)

    for _ in range(nrst):
        s = generate_initial_solution(V)
        for k in range(1, k_max):
            s_prime = shake(s, k)
            s_double_prime = vnd(s_prime, [n1, n2])
            if calculate_fitness(s_double_prime) < calculate_fitness(s):
                s = s_double_prime
                if calculate_fitness(s) < best_fitness:
                    best_solution = s
                    best_fitness = calculate_fitness(s)
    return best_solution, best_fitness

# Run the algorithm
best_solution, best_cost = gvns(list(range(1, n)), 100, 5)
best_solution.append(0)  # Closing the tour at the depot

print("Tour:", best_solution)
print("Total travel cost:", best_cost)