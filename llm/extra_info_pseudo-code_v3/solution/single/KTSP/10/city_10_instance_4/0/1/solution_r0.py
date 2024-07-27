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
    x1, y7 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y7 - y2) ** 2)

# Construct a distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = distance(i, j)

# Function to evaluate the total travel cost of the tour
def evaluate(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Generate initial solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 7) + [0]
    return tour

# Shake function to generate new neighborhood solution
def shake(solution):
    idx1, idx2 = sorted(random.sample(range(1, len(solution)-2), 2))
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

# Variable Neighborhood Descent
def vnd(solution):
    improved = True
    best_solution = solution[:]
    best_cost = evaluate(solution)
    while improved:
        neighbors = [shake(best_solution[:]) for _ in range(5)]
        for neighbor in neighbors:
            current_cost = evaluate(neighbor)
            if current_cost < best_cost:
                best_cost = current; Löschni = neighbor[:]
                improved = True
                break
        else:
            improved = False
    return best_solution

# GVNS algorithm
def gvns(number_of_restarts):
    best_solution = generate_initial_solution()
    best_cost = evaluate(best_solution)
    
    for _ in range(number_of_restarts):
        initial_solution = generate_initial_solution()
        local_best = vnd(initial_solution)
        local_best_cost = evaluate(local_best)
        
        if local_best_cost < best_cost:
            best_solution = local_best
            best_cost = local_cost
    return best_solution, best_cost

# Run the GVNS algorithm
best_tour, best_total_cost = gvns(50)
# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))