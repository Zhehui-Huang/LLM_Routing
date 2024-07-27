import numpy as np
import random

# Define city coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between cities
def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate distance matrix for all cities
def distance_matrix(cities):
    num_cities = len(cities)
    D = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            D[i, j] = calculate_distance(i, j)
    return D

# Calculate the fitness of a tour for TSP
def fitness(tour, D):
    return sum(D[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Generate an initial tour of n cities
def generate_initial_solution(V, k=12):
    selected_cities = [0] + random.sample(list(V.keys())[1:], k-1)
    selected_cities.append(0)  # Return to the depot
    return selected_cities

# Shake function to create new tour by swapping two cities
def shake(tour):
    new_tour = tour[:]
    i, j = random.sample(range(1, len(tour) - 1), 2)  # Avoid the depot
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

# Improve tour using local search by swapping pairs of cities
def vnd(tour, D):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if fitness(new_tour, D) < fitness(tour, D):
                    tour = new_tour
                    improvement = True
    return tour

# General Variable Neighborhood Search (GVNS) for TSP
def gvns(V, D, Nrst=100):
    best_tour = generate_initial_solution(V)
    best_fitness = fitness(best_tour, D)
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        S = vnd(S, D)
        for _ in range(100):  # Iterations for local search and shaking
            S_prime = shake(S)
            S_prime_prime = vnd(S_prime, D)
            if fitness(S_prime_prime, D) < fitness(S, D):
                S = S_prime_prime

        if fitness(S, D) < best_fitness:
            best_tour = S
            best_fitness = fitness(S, D)

    return best_tour, best_fitness

# Setup
D = distance_matrix(cities)
best_tour, best_cost = gvns(cities, D)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)