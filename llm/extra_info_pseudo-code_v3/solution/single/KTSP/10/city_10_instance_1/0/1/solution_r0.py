import numpy as np
import random

# City coordinates
coordinates = [
    (53, 68), (75, 11), (91, 95), (22, 80), 
    (18, 63), (54, 91), (70, 14), (97, 44), 
    (17, 69), (95, 89)
]

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Build distance matrix
def build_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = calculate_distance(coords[i], coords[j])
            else:
                distance_matrix[i][j] = 0.0
    return distance_matrix

# Generate initial random solution
def generate_initial_solution(num_cities, selected_k=5):
    cities = list(range(num_cities))
    random.shuffle(cities)
    cities.remove(0)  # Always including depot city at the front
    return [0] + cities[:selected_k-1] + [0]

# Calculate tour cost
def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Shake operation: random swap
def shake(solution):
    internal_cities = solution[1:-1]  # ignore depot
    a, b = random.sample(range(len(internal_cities)), 2)
    internal_cities[a], internal_cities[b] = internal_cities[b], internal_cities[a]
    return [0] + internal_cities + [0]

# Variable Neighborhood Descent
def vnd(solution, dist_matrix):
    improved = True
    while improved:
        improved = False
        best_cost = tour_cost(solution, dist_matrix)
        for i in range(1, len(solution)-3):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_solution[-1] = new_solution[0]  # Maintain cycle
                new_cost = tour_cost(new_solution, dist_matrix)
                if new_cost < best_cost:
                    solution = new_solution
                    best_cost = new_cost
                    improved = True
    return solution

# General Variable Neighborhood Search (GVNS)
def gvns(dist_matrix, num_restarts=10, num_cities=10):
    best_solution = None
    best_solution_cost = float('inf')
    
    for _ in range(num_restarts):
        current_solution = generate_initial_solution(num_cities)
        while True:
            new_solution = shake(current_solution)
            improved_solution = vnd(new_solution, dist_matrix)
            improved_solution_cost = tour_cost(improved_solution, dist_matrix)

            if improved_solution_cost < best_solution_cost:
                best_solution = improved_solution
                best_solution_cost = improved_solution_cost
                current_solution = improved_solution
            else:
                break
    
    return best_solution, best_solution_cost

# Utilizing the algorithm
distance_matrix = build_distance_matrix(coordinates)
best_tour, best_cost = gvns(distance_matrix, num_restarts=100)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)