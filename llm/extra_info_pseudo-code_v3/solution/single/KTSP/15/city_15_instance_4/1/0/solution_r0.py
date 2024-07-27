import numpy as np
import random

# Coordinates of cities including the depot
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance
def calc_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a distance matrix
def create_distance_matrix():
    n = len(coordinates)
    d_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                d_matrix[i, j] = calc_distance(i, j)
            else:
                d_matrix[i, j] = float('inf')
    return d_matrix

# Generate a random initial solution
def generate_initial_solution():
    cities = list(range(1, 15))
    selected_cities = random.sample(cities, 11)
    tour = [0] + selected_cities + [0]
    return tour

# Compute total travel distance
def tour_cost(tour):
    total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost

# Variable Neighborhood Descent
def VND(solution):
    best = solution
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best) - 1):
                if i != j:
                    new_tour = best[:]
                    new_tour[i], new_tour[j] = best[j], best[i]
                    if tour_cost(new_tour) < tour_cost(best):
                        best = new_tour
                        improved = True
    return best

# Shaking
def shake(solution, k=2):
    for _ in range(k):
        i, j = random.sample(range(1, len(solution) - 2), 2)
        solution[i], solution[j] = solution[j], solution[i]
    return solution

# General Variable Neighborhood Search
def GVNS(Nrst=100):
    S_best = generate_initial_solution()
    best_cost = tour_cost(S_best)
    
    for _ in range(Nrst):
        S = generate_initial_solution()
        k = 0
        while k < 20:  # termination criterion
            S_prime = shake(S[:], k)
            S_dprime = VND(S_prime)
            if tour_cost(S_dprime) < tour_cost(S):
                S = S_dprime
                k = 0
            else:
                k += 1
        if tour_cost(S) < best_cost:
            S_best = S
            best_cost = tour_cost(S)
    
    return S_best, best_cost

# Run GVNS
distance_matrix = create_distance_matrix()
best_tour, best_tour_cost = GVNS()

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)