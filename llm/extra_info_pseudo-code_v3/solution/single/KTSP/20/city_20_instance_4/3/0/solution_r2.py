import numpy as np
import random

# Coordinates of the cities
coordinates = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
               (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
               (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
               (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Number of cities including the depot
n = len(coordinates)

# Calculate the Euclidean distance matrix
distance_matrix = [[np.hypot(coordinates[i][0] - coordinates[j][0], coordinates[i][1] - coordinates[j][1]) for j in range(n)] for i in range(n)]

def generate_initial_solution():
    cities = list(range(1, n))  # do not include the depot city 0 initially
    selected_cities = [0] + random.sample(cities, 15)  # Choose 15 cities randomly and include depot
    return selected_cities + [0]  # append depot at the end as well for round trip

def calculate_cost(solution):
    return sum(distance_matrix[solution[i]][solution[i+1]] for i in range(len(solution)-1))

def shake(solution):
    idx1, idx2 = np.random.choice(range(1, len(solution)-1), 2, replace=False)
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

def local_search(solution):
    best_cost = calculate_cost(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):  # Exclude last element (return to depot)
            for j in range(i+1, len(solution)-1):  # Exclude first element (depot)
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    solution, best_cost = new_solution, new_cost
                    improved = True
    return solution

def GVNS(Nrst):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(Nrst):
        current_solution = generate_initial_solution()
        current_cost = calculate_cost(current_correction)

        while True:
            shaken_solution = shake(current_solution[:])
            improved_solution = local_search(shaken_solution)
            improved_cost = calculate_cost(improved_solution)

            if improved_cost < current_cost:
                current_solution, current_cost = improved_solution, improved_cost
                if improved_cost < best_cost:
                    best_solution, best_cost = improved_solution, improved_cost
            else:
                break  # Exit the while loop if no improvement

    return best_solution, best_cost

# Set number of restarts
Nrst = 100
best_solution, best_cost = GVNS(Nrst)

print("Tour:", best_solution)
print("Total travel cost:", round(best_cost, 2))