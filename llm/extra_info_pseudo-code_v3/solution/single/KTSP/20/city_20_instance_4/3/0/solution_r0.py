import numpy as np
import random

# Coordinates of the cities
coordinates = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
               (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
               (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
               (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Helper function to calculate Euclidean distance between two cities
def distance(i, j):
    return np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Compute distance matrix
n = len(coordinates)
distance_matrix = [[distance(i, j) for j in range(n)] for i in range(n)]

# Function to generate a random initial solution
def generate_initial_solution():
    cities = list(range(1, n))  # skipping the depot city 0
    selected_cities = [0] + random.sample(cities, 15)  # including depot city implicitly
    random.shuffle(selected_cities[1:])  # shuffle only non-depot cities
    return selected_cities + [0]

# Shaking function
def shake(solution):
    # Select two random indices to swap (excluding the depot at start and end)
    idx1, idx2 = np.random.choice(range(1, 16), 2, replace=False)
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

# Variable Neighborhood Descent
def VND(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, 16):
            for j in range(i+1, 16):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_cost(new_solution) < calculate_cost(solution):
                    solution = new_solution
                    improved = True
    return solution

# Function to calculate the tour cost
def calculate_cost(solution):
    return sum(distance_matrix[solution[i]][solution[i+1]] for i in range(len(solution)-1))

# General Variable Neighborhood Search (GVNS)
def GVNS(Nrst):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    for _ in range(Nrst):
        current_solution = generate_initial_solution()
        while True:
            new_solution = shake(current_solution)
            new_solution = VND(new_solution)
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                break  # reset and restart the loop
            else:
                current_solution = new_solution  # continue shaking
    return best_solution, best_cost

# Execute the algorithm
best_sol, best_sol_cost = GVNS(100)
print("Tour:", best_sol)
print("Total travel cost:", best_sol_cost)