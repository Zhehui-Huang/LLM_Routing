import random
import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def generate_distance_matrix(cities):
    num_cities = len(cities)
    D = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            D[i][j] = euclidean_distance(cities[i], cities[j])
    return D

def total_cost(tour, D):
    return sum(D[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def generate_initial_solution(V):
    tour = [0] + random.sample(V[1:], 3)
    tour.append(0)
    return tour

def shake(S, V, D):
    new_tour = [0]
    candidates = list(set(range(1, len(V))) - set(S[1:-1]))
    new_tour += random.sample(S[1:-1] + random.sample(candidates, 1), 3)
    new_tour.append(0)
    return new_tour

def vnd(S, D):
    best_tour = S[:]
    best_cost = total_cost(S, D)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 2):
            for j in range(i+1, len(S) - 1):
                if i != 1 or j != len(S) - 2:  # Exclude depot city from swapping
                    new_tour = S[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = total_cost(new_tour, D)
                    if new_cost < best_cost:
                        best_tour, best_cost = new_tour[:], new_cost
                        improved = True
    return best_tour

def gvns(V, D, Nrst):
    best_solution = generate_initial_solution(V)
    best_cost = total_cost(best_solution, D)
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        while True:
            S_prime = shake(S, V, D)
            S_double_prime = vnd(S_prime, D)
            new_cost = total_cost(S_double_prime, D)
            if new_cost < best_cost:
                best_solution, best_cost = S_double_prime[:], new_cost
                break  # Reset the loop
            else:
                # No improvement found, switch out
                break
    return best_solution, best_cost

cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]
distance_matrix = generate_distance_matrix(cities)

# Execute GVNS algorithm
solution, solution_cost = gvns(cities, distance_matrix, 100)

# Output results formatted as per requirements
print(f"Tour: {solution}")
print(f"Total travel cost: {solution_cost:.2f}")