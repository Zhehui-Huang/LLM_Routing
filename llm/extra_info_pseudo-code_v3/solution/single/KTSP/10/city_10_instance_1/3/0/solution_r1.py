import numpy as np
import random
from math import sqrt

# Define the coordinates of the cities
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
    8: (17, 69), 9: (95, 89)
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
    path = [0] + random.sample([x for x in V if x != 0], 4)
    path.append(0)  # Close the loop
    return path

# Shake the solution
def shake(S):
    internal_cities = S[1:-1]  # Exclude the depot
    random.shuffle(internal_cities)
    new_S = [S[0]] + internal_cities + [S[0]]
    return new_S

# Calculate the total distance of the tour
def calculate_distance(path, distance_matrix):
    return sum(distance_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))

# Simple VND function with a two-city swap method
def vnd(S, distance_matrix):
    for i in range(1, len(S)-2):
        for j in range(i+1, len(S)-1):
            new_S = S[:]
            new_S[i], new_S[j] = new_S[j], new_S[i]
            new_dist = calculate_distance(new_S, distance_matrix)
            if new_dist < calculate_distance(S, distance_matrix):
                return new_S
    return S

# GVNS algorithm
def gvns(Nrst, cities, distance_matrix):
    best_solution = generate_initial_solution(cities.keys())
    best_distance = calculate_distance(best_solution, distance_matrix)
    
    for _ in range(Nrst):
        S = generate_initial_solution(cities.keys())
        while True:
            S_prime = shake(S)
            S_double_prime = vnd(S_prime, distance_matrix)
            if calculate_distance(S_double_prime, distance_matrix) < best_distance:
                S = S_double_prime
                best_distance = calculate_distance(S, distance_matrix)
                best_solution = S[:]
            else:
                break

    return best_solution, best_distance

# Solve the problem with the number of restarts
Nrst = 100
result_tour, result_cost = gvns(Nrst, cities, distance_matrix)
print("Tour:", result_tour)
print("Total travel cost:", result_cost)