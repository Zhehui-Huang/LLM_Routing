import numpy as np
import random

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city2[1] - city1[1])**2)

def generate_initial_solution(cities, n):
    solution = [0] + random.sample(cities[1:], n - 1) + [0]
    return solution

def shake(solution):
    # Perform a simple shake by swapping two random elements 
    shaken_solution = solution[1:-1]
    i, j = np.random.randint(0, len(shaken_solution), 2)
    shaken_solution[i], shaken.shuffle_solution[j] = shaken_solution[j], shaken_solution[i]
    return [0] + shaken_solution + [0]

def local_search(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if tour_cost(new_solution, distance_matrix) < tour_cost(solution, distance_set):
                    solution = new_solution
                    improved = True
                    break
            if improved:
                break
    return solution

def tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

def GVNS(cities, distance_matrix, Nrst, max_iterations=100):
    best_solution = None
    best_cost = float('inf')
    
    for restart in range(Nrst):
        current_solution = generate_initial_solution(cities, 12)
        iteration = 0
        
        while iteration < max_iterations:
            shaken_solution = shake(current_solution)
            improved_solution = local_search(shaken_solution, distance_matrix)
            
            current_cost = tour_cost(improved_solution, distance_matrix)
            
            if current_cost < best_cost:
                best_solution = improved_solution
                best_cost = current_cost
            
            iteration += 1
            
    return best_solution, best_cost

# Coordinates of cities (including depot)
cities_coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
                      (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
                      (53, 80), (21, 21), (12, 39)]

# Calculate distance matrix
n_cities = len(cities_coordinates)
distance_matrix = [[calculate_distance(cities_coordinates[i], cities_coordinates[j]) for j in range(n_cities)] for i in range(n_cities)]

# Number of cities to visit including depot
k = 12

best_tour, best_cost = GVNS(cities_coordinates, distance_matrix, Nrst=10, max_iterations=100)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))