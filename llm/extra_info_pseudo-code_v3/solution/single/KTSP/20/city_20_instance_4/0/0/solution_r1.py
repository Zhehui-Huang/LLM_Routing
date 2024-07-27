import numpy as np
import random

# Coordinates of all cities including depot
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Create a distance matrix
n_cities = len(coordinates)
distance_matrix = [[euclidean_distance(i, j) for j in range(n_cities)] for i in range(n_cities)]

# Generate initial random solution
def generate_initial_solution():
    cities = list(range(1, n_cities))
    random.shuffle(cities)
    return [0] + cities[:15] + [0]

# Calculate tour cost
def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Shaking method by swap
def shake(solution):
    n = len(solution)
    i, j = random.sample(range(1, n-1), 2)
    new_solution = solution[:]
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Local search using a simple 2-opt method
def local_search(solution):
    best_cost = calculate_cost(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                if j-i == 1: continue
                new_solution = solution[:]
                new_solution[i:j] = solution[j-1:i-1:-1]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
                    improved = True
        solution = best_solution
    return solution

# GVNS algorithm implementation
def gvns(max_iterations=50):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    for _ in range(max_iterations):
        current_solution = shake(best_solution)
        current_solution = local_search(current_solution)
        current_cost = calculate_cost(current_solution)
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_solution
    return best_solution, best_cost

# Get best tour and cost
best_tour, best_cost = gvns(max_iterations=1000)

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.4f}")