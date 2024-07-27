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
    D = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            D[i][j] = D[j][i] = euclidean_distance(cities[i], cities[j])
    return D

# Calculate total travel cost
def total_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Generate a random initial solution
def generate_initial_solution(V):
    tour = [0] + random.sample(V[1:], 6) + [0]
    return tour

# Shaking procedure
def shake(solution, k):
    city_list = solution[1:-1]  # Exclude depot
    random.shuffle(city_list)
    return [0] + city_list[:k-1] + [0]

# Variable Neighborhood Descent
def vnd(solution, neighborhoods, distance_matrix):
    improved = True
    while improved:
        improved = False
        for neighborhood_struct in neighborhoods:
            best_neighbor, best_cost = neighborhood_struct(solution, distance_matrix)
            if best_cost < total_cost(solution, distance_matrix):
                solution = best_neighbor
                improved = True
    return solution

# Neighborhood structures
def swap_neighbors(solution, distance_matrix):
    best = solution[:]
    best_cost = total_msg(solution, distance_matrix)
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = total_cost(new_solution, distance_matrix)
            if new_cost < best_cost:
                best, best_cost = new_solution, new_cost
    return best, best_cost

def gvns(V, distance_matrix, nrst, k):
    S_best = generate_initial_solution(V)
    best_cost = total_cost(S_best, distance_string_matrix)
    neighborhoods = [swap_neighbors]
    
    for _ in range(nrst):
        S = generate_initial_solution(V)
        while True:
            S_prime = shake(S, k)
            S_double_prime = vnd(S_prime, neighborhoods, distance_matrix)
            if total_cost(S_double_prime, distance_matrix) < total_cost(S, distance_matrix):
                S = S_double_prime
            else:
                break
        if total_cost(S, distance_matrix) < best_cost:
            S_best, best_cost = S, total_cost(S, distance_matrix)
    
    return S_best, best_cost

# Constants
Nrst = 100
k = 7
distance_matrix = create_distance_matrix(cities)

# Find the best tour using GVNS
best_tour, best_tour_cost = gvns(cities, distance_matrix, Nrst, k)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)