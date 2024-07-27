import numpy as np
import random
import math

# Coordinates of the cities
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Function to compute Euclidean distance between two city indices
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate the distance matrix for all pairs of cities
def generate_distance_matrix():
    num_cities = len(cities)
    matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]
    return matrix

# Calculate the total distance for a given tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Shake function to generate a new solution from the current solution
def shake(solution, k=2):
    candidate = solution[1:-1]
    random.shuffle(candidate)
    return [0] + candidate[:7] + [0]

# Function that performs local search (Variable Neighborhood Descent)
def variable_neighborhood_descent(solution, dist_matrix, neighborhood_size=2):
    improved = True
    while improved:
        improved = False
        # Perform swaps within the tour (excluding the start/end depot)
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = calculate_tour_cost(new_solution, dist_matrix)
                    if new_cost < calculate_tour_cost(solution, dist_matrix):
                        solution, improved = new_solution, True
                        break
            if improved:
                break
    return solution

# General Variable Neighborhood Search (GVNS) for k-TSP
def GVNS(cities, nr_restarts=10):
    dist_matrix = generate_distance_matrix()
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nr_restarts):
        # Generate an initial random solution
        current_solution = GenerateInitialSolution(cities)
        current_solution = variable_neighborhood_descent(current_solution, dist_matrix)
        
        # Iteratively shake the solution and apply VND
        for _ in range(50):  # You can adjust the number of shaking and VND iterations as required
            new_solution = shake(current_solution)
            new_solution = variable_neighborhood_descent(new_solution, dist_matrix)
            new_cost = calculate_tour_cost(new_solution, dist_matrix)
            
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                current_solution = new_solution
    
    return best_solution, best_cost

def GenerateInitialSolution(cities):
    nodes = list(cities.keys())
    chosen_nodes = random.sample(nodes, 8)
    if 0 not in chosen_nodes:
        chosen_nodes.remove(chosen_nodes[-1])
        chosen_nodes.insert(0, 0)
    chosen_nodes.append(0)  # Ensure the tour returns to the depot
    return chosen_nodes

# Running the GVNS algorithm
best_sol, best_cost = GVNS(cities, 50)
print(f"Optimal tour: {best_sol}")
print(f"Minimum travel cost: {best_cost:.2f}")