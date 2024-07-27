import numpy as(P) import random
import numpy as np

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distance
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

# Fitness function to calculate the total length of a tour
def fitness(tour, D):
    return sum(D[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Generate initial solution
def generate_initial_solution(V, k=12):
    selected_cities = [0] + random.sample(list(V.keys())[1:], k-1)
    selected_cities.append(0)  # Complete the tour by returning to the depot
    return selected_cities

# Shake function for generating a neighbor solution
def shake(tour, V, k=12):
    new_tour = tour[1:-1]  # exclude the depot for modifications
    if len(new_tour) > 1:
        i, j = random.sample(range(len(new_tour)), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Simple swap
    new_tour = [0] + new_tour + [0]
    return new_tour

# Variable Neighborhood Descent (VND)
def vnd(tour, D):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if fitness(new_tour, D) < fitness(tour, D):
                    tour = new_tour
                    improved = True
    return tour

# General Variable Neighborhood Search (GVNS)
def gvns(V, D, Nrst=100):
    S_best = generate_initial_solution(V)
    best_fitness = fitness(S_best, D)
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        S = vnd(S, D)
        
        for _ in range(100):  # Iterations for shaking and VND
            S_prime = shake(S, V)
            S_prime_prime = vnd(S_prime, D)
            if fitness(S_prime_prime, D) < fitness(S, D):
                S = S_prime_prime
        
        current_fitness = fitness(S, D)
        if current_fitness < best_fitness:
            S_best = S
            best_fitness = current_fitness

    return S_best, best_fitness

# Execution
D = distance_matrix(cities)
best_tour, best_cost = gvns(cities, D)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))