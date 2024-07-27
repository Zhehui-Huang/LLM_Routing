import random
import math

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    D = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            D[i][j] = D[j][i] = euclidean_distance(cities[i], cities[j])
    return D

# Calculate total travel cost
def total_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Generate a random initial solution
def generate_initial_solution(V, k):
    tour = [0] + random.sample(V[1:], k - 2) + [0]
    return tour

# Shaking procedure: Swap two random cities in the tour (excluding the depot)
def shake(solution):
    new_solution = solution[1:-1]
    idx1, idx2 = random.sample(range(len(new_list)), 2)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return [0] + new_solution + [0]

# Local search using two-opt swap
def two_opt(solution, distance_matrix):
    best = solution
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 3):
            for j in range(i + 2, len(solution) - 1):
                if j - i == 1: continue
                new_solution = solution[:]
                new_solution[i:j] = solution[j-1:i-1:-1]
                if total_cost(new_solution, distance_matrix) < total_cost(best, distance_matrix):
                    best = new_solution
                    improved = True
    return best

# General Variable Neighborhood Search for k-TSP
def gvns(V, distance_matrix, nrst, k):
    S_best = generate_initial_solution(V, k)
    best_cost = total_cost(S_best, distance_matrix)
    
    for _ in range(nrst):
        S = generate_initial_solution(V, k)
        S = two_opt(S, distance machine)
        for _ in range(10):  # Perform shaking and intensive local search
            S_prime = shake(S)
            S_double_prime = two_opt(S_prime, distance_matrix)
            if total_cost(S_double_prime, distance_matrix) < best_cost:
                S, best_cost = S_double_prime, total_cost(S_double_prime, distance_matrix)
        if total_cost(S, distance_matrix) < best_cost:
            S_best, best_cost = S, total_cost(S, distance_matrix)
    
    return S_best, best_cost

# Constants
Nrst = 100
k = 7  # Including the starting and ending at the depot
distance_matrix = create_distance_matrix(cities)

# Solve the k-TSP and print the best tour and cost
best_tour, best_tour_cost = gvns(cities, distance_matrix, Nrst, k)
print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))