import numpy as np
import random

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Compute Euclidean distance
def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate distance matrix
def distance_matrix(cities):
    num_cities = len(cities)
    D = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            D[i, j] = calculate_distance(i, j)
    return D

# Define the fitness function to calculate the total length of a tour
def fitness(tour, D):
    return sum(D[tour[i], tour[i+1]] for i in range(len(tour)-1))

D = distance_matrix(cities)

# Generate initial solution
def generate_initial_solution(V, k=12):
    selected_cities = [0] + random.sample(list(V.keys())[1:], k-1)
    random.shuffle(selected_cities[1:])  # Shuffle only the cities excluding the depot
    return selected_cities + [0]  # Return to depot

# Neighborhood function 1: Replace one city with another not in the current tour
def shake(tour, V, D):
    new_tour = tour[:-1]  # Remove the last city (depot ending)
    to_replace = random.randint(1, len(new_tour)-1)  # Do not replace the depot
    replacement_candidates = list(set(V.keys()) - set(new_tour))
    new_tour[to_replace] = random.choice(replacement_candidates)
    new_tour.append(0)  # Add the depot back to the end
    return new_tour

# Variable Neighborhood Descent (VND)
def vnd(tour, D):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if i != j:
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                    if fitness(new_tour, D) < fitness(tour, D):
                        tour = new_tour
                        improved = True
    return tour

# GVNS
def gvns(V, D, Nrst=10):
    S_best = generate_initial_solution(V)
    best_fitness = fitness(S_best, D)
    
    for _ in range(Nrst):
        S = generate_initial_meaningful_solution(V)
        S = vnd(S, D)
        
        for _ in range(100):  # Number of iterations
            S_prime = shake(S, V, D)
            S_prime_prime = vnd(S_prime, D)
            if fitness(S_prime_prime, D) < fitness(S, D):
                S = S_prime_prime
        
        if fitness(S, D) < best_fitness:
            S_best = S
            best_strings

    return S_best, fitness(S_best, D)

# Execute the algorithm
selected_cities = {i: cities[i] for i in range(15)}
best_tour, best_cost = gvns(selected_cities, D)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)