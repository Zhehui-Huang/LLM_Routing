import numpy as np
import random

# City coordinates: index corresponds to city number
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate distance matrix
n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Solution Encoding: Represent solutions as list of indices, starting and ending with the depot city
# Initial Solution Generation
def generate_initial_solution(num_cities, k=7):
    solution = [0]  # Start at the depot
    available_cities = list(range(1, num_cities))
    selected_cities = random.sample(available_cities, k-1)
    solution.extend(selected_cities)
    solution.append(0)  # End at the depot
    return solution

# Fitness function to calculate total travel cost
def calculate_fitness(solution):
    total_cost = sum(distance_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1))
    return total_cost

# Shaking - Changing the solution within a neighborhood structure
def shake(solution):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [solution[0]] + new_solution + [solution[0]]

# Variable Neighborhood Descent using two neighborhood structures N1 and N2
def vnd(solution):
    improved = True
    while improved:
        current_cost = calculate_fitness(solution)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = calculate_fitness(new_solution)
                    if new_cost < current_cost:
                        solution = new_solution
                        current_cost = new_cost
                        improved = True
                        break
            else:
                continue
            break
        else:
            improved = False
    return solution

# GVNS algorithm approach
def gvns(num_restarts, num_cities):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        solution = generate_initial_solution(num_cities)
        solution = vnd(solution)
        
        iter_no_change = 0
        while iter_no_change < 100:  # Termination criteria can also be a time limit
            new_solution = shake(solution)
            new_solution = vnd(new_solution)
            new_cost = calculate_fitness(new_solution)
            if new_cost < calculate_fitness(solution):
                solution = new_solution
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = solution
                iter_no_change = 0
            else:
                iter_no_change += 1
                
    return best_solution, best_cost

best_solution, best_cost = gvns(100, n_cities)
print(f"Tour: {best_solution}")
print(f"Total travel cost: {best_cost:.2f}")