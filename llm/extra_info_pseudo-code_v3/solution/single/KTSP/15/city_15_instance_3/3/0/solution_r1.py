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
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Generate a random initial solution that includes the depot
def generate_initial_solution(V):
    selected_indices = sample(range(1, len(V)), 9)  # Select 9 cities excluding depot
    path = [0] + [V[i] for i in selected_indices]
    return path

# Calculate the fitness of a solution
def calculate_fitness(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += distance_matrix[solution[i]][solution[i + 1]]
    total_distance += distance_matrix[solution[-1]][solution[0]]  # return to the depot
    return total_distance

# Define neighborhood structures
def swap(solution):
    n = len(solution)
    for i in range(1, n-1):
        for j in range(i+1, n):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            yield new_solution

def reverse(solution):
    n = len(solution)
    for i in range(1, n-2):
        for j in range(i+2, n):
            new_solution = solution[:]
            new_solution[i:j] = reversed(new_solution[i:j])
            yield new_solution

# Performing the VND
def vnd(solution):
    neighborhoods = [swap, reverse]
    current_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for neighborhood in neighborhoods:
            for candidate in neighborhood(current_solution):
                if calculate_fitness(candidate) < calculate_fitness(current_solution):
                    current_solution = candidate
                    improved = True
                    break
            if improved:
                break
    return current_solution

# Shaking operation
def shake(solution, k):
    indices = sample(range(1, len(solution)), k)  # choose k random indices to swap (excluding depot)
    for i in range(0, k-1, 2):
        solution[indices[i]], solution[indices[i+1]] = solution[indices[i+1]], solution[indices[i]]
    return solution

# Perform GVNS
def gvns(V, nrst, k_max):
    best_solution = generate_initial_solution(V)
    best_fitness = calculate_fitness(best_solution)

    for _ in range(nrst):
        k = 1
        s = generate_initial_solution(V)
        while k <= k_max:
            s_prime = shake(s[:], k)  # shake using deep copy to preserve s
            s_double_prime = vnd(s_prime)
            if calculate_fitness(s_double_prime) < calculate_fitness(s):
                s = s_double_prime[:]
                k = 1
                if calculate_fitness(s) < best_fitness:
                    best_solution = s[:]
                    best_fitness = calculate_fitness(s)
            else:
                k += 1

    return best_solution, best_fitness

# Run the algorithm
city_indices = list(range(n))  # city indices
best_solution, best_cost = gvns(city_indices, 100, 5)

print("Tour:", best_solution)
print("Total travel cost:", round(best_cost, 2))