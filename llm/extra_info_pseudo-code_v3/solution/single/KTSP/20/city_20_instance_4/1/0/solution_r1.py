import numpy as np
import random

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Helper function to calculate Euclidean distance
def dist(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                   (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Number of cities to visit including the depot
k = 16

# Generate initial solution
def generate_initial_solution():
    solution = [0] + random.sample(range(1, 20), k - 1)
    return solution

# Calculate the total distance of the tour
def calculate_total_distance(tour):
    total_dist = sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1)) + dist(tour[-1], tour[0])
    return total_dist

# VND handling two types of neighborhood structures
def vnd(solution):
    improved = True
    while improved:
        improved = False
        # N1 structure: swap any two cities
        for i in range(1, k):
            for j in range(i + 1, k):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_distance(new_solution + [new_solution[0]]) < calculate_total_distance(solution + [solution[0]]):
                    solution = new_solution
                    improved = True
                    break
            if improved:
                break
    return solution

# Shake by swapping two random cities
def shake(solution):
    new_solution = solution[:]
    i, j = random.sample(range(1, k), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# GVNS loop
def gvns(nrst):
    best_solution = generate_initial_solution()
    best_cost = calculate_total_distance(best_solution + [best_solution[0]])

    for _ in range(nrst):
        current_solution = generate_initial_solution()
        current_cost = calculate_total_distance(current_solution + [current_solution[0]])
        
        while True:
            candidate_solution = shake(current_solution)
            candidate_solution = vnd(candidate_solution)
            candidate_cost = calculate_total_distance(candidate_solution + [candidate_solution[0]])
            
            if candidate_cost < current_cost:
                current_solution, current_cost = candidate_solution, candidate_cost
            else:
                break
        
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost

    return best_solution, best_cost

n_restarts = 100
solution, cost = gvns(n_restarts)
solution.append(0)  # Closing the tour by returning to the depot

print("Tour:", solution)
print("Total travel cost:", round(cost, 2))