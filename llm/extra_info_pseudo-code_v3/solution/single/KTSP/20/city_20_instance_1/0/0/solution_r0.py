import numpy as np
import random

# Define city coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Number of cities including the depot city
n = 20

# Calculate euclidean distance between two cities
def euclidean(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create distance matrix
D = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        D[i, j] = euclidean(cities[i], cities[j])

# Successive modifications for solution quality improvement
def shake(solution):
    idx = list(range(1, 7))
    random.shuffle(idx)
    new_solution = [solution[i] for i in idx]
    new_solution.insert(0, 0)  # Ensure starting at the depot
    new_solution.append(0)     # Ensure ending at the depot
    return new_solution

def VND(solution, D):
    improved = True
    while improved:
        improved = False
        for i in range(1, 6):  # Explore neighborhoods
            for j in range(i + 1, 7):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_cost(new_solution, D) < calculate_cost(solution, D):
                    solution = new_solution
                    improved = True
    return solution

def calculate_cost(solution, D):
    return sum(D[solution[i], solution[i + 1]] for i in range(len(solution) - 1))

# Generate a random initial solution
def generate_initial_solution():
    selected_cities = random.sample(range(1, n), 6) + [0]
    selected_cities.append(0)  # Return to start
    return selected_cities

# GVNS algorithm
def GVNS(Nrst, D):
    best_solution = None
    best_cost = float('inf')
    for _ in range(Nrst):
        solution = generate_initial_solution()
        for _ in range(100):  # Termination condition as max iterations
            new_solution = shake(solution)
            new_solution = VND(new_solution, D)
            cost = calculate_cost(new_solution, D)
            if cost < best_cost:
                best_solution, best_cost = new_solution, cost
                break
            else:
                continue
    return best_solution, best_cost

# Finding the optimal route and cost
best_solution, best_cost = GVNS(10, D)
print("Tour:", best_solution)
print("Total travel cost:", round(best_cost, 2))