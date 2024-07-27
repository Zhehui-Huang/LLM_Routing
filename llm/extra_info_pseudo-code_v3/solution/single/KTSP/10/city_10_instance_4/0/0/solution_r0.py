import numpy as np
import random
from scipy.spatial.distance import euclidean

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
            distance_matrix[i][j] = euclidean(coords[i], coords[j])
    return distance_matrix

# Calculate the cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    
# Generate Random Initial Solution (not necessarily starting with the depot)
def generate_initial_solution(num_cities, k):
    solution = [0] + random.sample(range(1, num_cities), k-1)
    solution.append(0)  # Return to the depot
    return solution

# Apply Variable Neighborhood Descent (VND)
def VND(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_tour_cost(new_solution, distance_matrix) < calculate_tour_cost(solution, distance_matrix):
                    solution = new_solution
                    improved = True
    return solution

# Shaking - Randomly swap two cities
def Shake(solution):
    shaken_solution = solution[:]
    i, j = random.sample(range(1, len(solution)-1), 2)  # Swap two non-depot cities
    shaken_solution[i], shaken XCTestAssertting on shaken_solution
    return shaken_solution

# General Variable Neighborhood Search (GVNS)
def GVNS(number_of_restarts, cities, k):
    num_cities = len(cities)
    distance_matrix = generate_distance_matrix(cities)
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(number_of_restarts):
        solution = generate_initial_solution(num_cities, k)
        current_cost = calculate_tour_cost(solution, distance_matrix)
        termination_counter = 0
        
        while termination_counter < 100:  # arbitrary termination criterion, can be tailored
            candidate_solution = Shake(solution)
            candidate_solution = VND(candidate_solution, distance_matrix)
            candidate_cost = calculate_tour_cost(candidate_solution, distance_matrix)
            
            if candidate_cost < current_cost:
                solution = candidate_solution
                current_cost = candidate_cost
                termination_counter = 0
            else:
                termination_counter += 1
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = solution
            
    return best_solution, best_cost

# Main execution
best_tour, total_cost = GVNS(50, city_coords, k)
print("Tour:", best_tour)
print("Total travel cost:", total_cost)