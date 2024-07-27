import numpy as np
import random
from math import sqrt

# Coordinates of the cities
city_coords = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Number of cities to visit, including the depot
k = 8

# Generate the distance matrix
def generate_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return distance_matrix

# Calculate the cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
# Generate Initial Solution
def generate_initial_solution(num_cities, k):
    solution = [0] + random.sample(range(1, num_cities), k-1)
    solution.append(0)  # Return to the depot
    return solution

# Variable Neighborhood Descent (VND)
def VND(solution, distance_matrix):
    best_solution = solution[:]
    best_cost = calculate_tour_cost(best_solution, distance_matrix)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_tour_cost(new_solution, distance_matrix)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
    
    return best_solution

# Shaking - Randomly swap two cities
def Shake(solution):
    shaken_solution = solution[:]
    i, j = random.sample(range(1, len(solution)-1), 2)  # Swap two non-depot cities
    shaken_solution[i], shaken_solution[j] = shaken_solution[j], shaken_solution[i]
    return shaken_solution

# General Variable Neighborhood Search (GVNS)
def GVNS(number_of_restarts, cities, k):
    num_cities = len(cities)
    distance_matrix = generate_distance_matrix(cities)
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(number_of_restarts):
        solution = generate_initial_solution(num_cities, k)
        solution = VND(solution, distance_matrix)
        current_cost = calculate_tour_cost(solution, distance_matrix)
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = solution[:]
            
        for _ in range(100):  # termination condition can be more sophisticated
            new_solution = Shake(solution)
            new_solution = VND(new_solution, distance_matrix)
            new_cost = calculate_tour_cost(new_solution, distance_matrix)
            
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    
    return best_solution, best_cost

# Main execution
best_tour, total_cost = GVNS(10, city_coords, k)  # Includes reduced number of restarts for quick run
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))