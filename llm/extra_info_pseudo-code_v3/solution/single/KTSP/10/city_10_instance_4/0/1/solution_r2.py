import numpy as np
import random
import math

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Construct a distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = distance(i, j)

# Function to evaluate the total travel cost of the tour
def evaluate(tour):
    total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    return total_cost

# Generate initial solution
def generate_initial_solution():
    selected_cities = random.sample(list(cities.keys())[1:], 7)
    tour = [0] + selected_cities + [0]
    return tour

# Shake function
def shake(solution):
    new_solution = solution[:]
    idx1, idx2 = sorted(random.sample(range(1, len(solution)-1), 2))
    new_solution[idx1], new_solution[idx2] = solution[idx2], solution[idx1]
    return new_solution

# Variable Neighborhood Descent
def vnd(solution):
    best_solution = solution
    best_cost = evaluate(solution)
    for _ in range(20):
        neighbor = shake(best_solution)
        neighbor_cost = evaluate(neighbor)
        if neighbor_cost < best_cost:
            best_solution = neighbor
            best_cost = neighbor_cost
    return best_solution

# General Variable Neighborhood Search (GVNS)
def gvns(restarts):
    best_solution = generate_initial_solution()
    best_cost = evaluate(best_solution)
    
    for _ in range(restarts):
        new_solution = generate_initial_solution()
        refined_solution = vnd(new_solution)
        refined_cost = evaluate(refined_solution)
        
        if refined_cost < best_cost:
            best_solution = refined_solution
            best_cost = refined_cost
    
    return best_solution, best_cost

# Execute the algorithm
best_tour, best_total_cost = gvns(50)
# Print the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))