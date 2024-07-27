import random
import math
from itertools import permutations

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the initial random solution
def generate_initial_solution(home, other_cities):
    cities = [home] + random.sample(other_cities, 4) + [home]
    return cities

# Calculate the total cost of the tour
def calculate_total_cost(tour, city_coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return total_cost

# Perform the local search to find a better solution
def local_search(solution, city_coords):
    best_solution = solution[:]
    best_cost = calculate_total_cost(best_solution, city_coords)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = calculate_total_cost(new_solution, city_coords)
                    if new_cost < best_cost:
                        best_solution = new_solution[:]
                        best_cost = new_cost
                        improved = True
    return best_solution, best_cost

# Shaking solution by swapping two random cities
def shake(solution):
    shaken_solution = solution[:]
    idx1, idx2 = random.sample(range(1, len(solution) - 2), 2)
    shaken_solution[idx1], shaken_solution[idx2] = shaken_solution[idx2], shaken_solution[idx1]
    return shaken_solution

# GVNS Algorithm for k-TSP
def GVNS(city_coords, nrst=100):
    home = city_coords[0]
    other_cities = city_coords[1:]
    best_solution = []
    best_cost = float('inf')
    
    for _ in range(nrst):
        # Generate an initial random solution
        current_solution = generate_initial_solution(home, other_cities)
        current_cost = calculate_total_cost(current_solution, city_coords)
        
        # Local search
        current_solution, current_cost = local_search(current_solution, city_coords)
        
        # Iterative improvement
        for _ in range(100):  # Max iterations for the shake-local search steps
            shaken_solution = shake(current_solution)
            improved_solution, improved_cost = local_search(shaken_solution, city_coords)
            if improved_cost < best_cost:
                best_solution, best_response = improved_solution, improved_cost
                break
            current_solution = improved_solution
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# City coordinates
city_coordinates = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
                    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
                    (83, 96), (60, 50), (98, 1)]
# Solve the problem using GVNS
best_tour, tour_cost = GVNS(city_coordinates)

# Output results
print("Tour:", best_tour)
print("Total travel cost:", tour_cost)