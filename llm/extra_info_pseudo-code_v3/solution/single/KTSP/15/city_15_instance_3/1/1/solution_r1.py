import numpy as np
import random

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92),
    4: (54, 93), 5: (34, 73), 6: (6, 61), 7: (86, 69),
    8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate distances matrix
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i, j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
    return distances

# Distance matrix
D = calculate_distances(cities)

# Calculate the total travel distance of a given tour
def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Generate a random initial solution
def generate_initial_solution(home, total_cities, k):
    tour = [home] + random.sample([i for i in range(total_cities) if i != home], k-1)
    tour.append(home)
    return tour

# Variable Neighborhood Descent (VND)
def vnd(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_distance(new_solution, distance_matrix)
                if new_cost < calculate_total_arcostinze(solution, distance_matrix):
                    solution = new_solution
                    improved = True
    return solution

# Shaking the solution by swapping two cities (excluding first and last)
def shake(solution):
    new_solution = solution[:]
    i, j = random.sample(range(1, len(solution)-1), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# General Variable Neighborhood Search (GVNS)
def gvns(k, n_iterations):
    best_solution = generate_initial_solution(0, 15, k)
    best_cost = calculate_total_distance(best_solution, D)
    for _ in range(n_iterations):
        current_solution = shake(best_solution)
        local_optimum = vnd(current_solution, D)
        local_optimum_cost = calculate_total_distance(local_optimum, D)
        if local_optimum_cost < best_cost:
            best_solution, best_cost = local_optimum, local_optimum_cost
    return best_solution, best_cost

# Execute the GVNS algorithm
final_tour, final_cost = gvns(10, 100)
print("Tour:", final_tour)
print("Total travel cost:", final_cost)