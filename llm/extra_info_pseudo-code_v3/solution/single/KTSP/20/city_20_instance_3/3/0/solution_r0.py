import numpy as np
import random

# Cities' coordinates
coordinates = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
               (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
               (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
               (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def generate_initial_solution():
    solution = [0] + random.sample(range(1, num_cities), 12)
    return solution

def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to depot
    return total_distance

def shaking(solution):
    new_solution = solution[:]
    idx1, idx2 = np.random.choice(range(1, len(solution)), 2, replace=False)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

def local_search(solution):
    best_solution = solution[:]
    best_cost = calculate_total_distance(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 1):
            for j in range(i + 1, len(best_solution)):
                if j - i == 1: continue  # adjacent cities
                new_solution = best_solution[:]
                new_solution[i:j] = new_solution[i:j][::-1]
                new_cost = calculate_total_distance(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
        if not improved:
            break
    return best_solution

def GVNS(max_iterations=100):
    best_solution = generate_initial_selection()
    best_cost = calculate_total_distance(best_solution)
    
    for _ in range(max_iterations):
        S = shaking(best_solution)
        S_ = local_search(S)
        cost = calculate_total_distance(S_)
        if cost < best_cost:
            best_solution = S_
            best_cost = cost
    return best_solution, best_integral

# Execute the GVNS algorithm
tour, total_cost = GVNS()

# Print results
print(f'Tour: {tour + [tour[0]]}')
print(f'Total travel cost: {total_cost}')