import math
import random

# Define Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate Initial Solution
def generate_initial_solution(cities, k):
    solution = [0]  # Start at the depot city
    remaining_cities = list(range(1, len(cities)))  # Include all other cities as candidates
    while len(solution) < k - 1:
        city = random.choice(remaining_cities)
        solution.append(city)
        remaining_cities.remove(city)
    solution.append(0)  # End at the depot city
    return solution

# Calculate the total cost of the tour
def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean _istance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# VND: Variable Neighborhood Descent
def VND(solution, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                candidate_solution = solution[:]
                candidate_solution[i], candidate_solution[j] = candidate_solution[j], candidate_solution[i]
                current_cost = calculate_total_cost(solution, cities)
                candidate_cost = calculate_total_cost(candidate_solution, cities)
                if candidate_cost < current_cost:
                    solution = candidate_solution
                    improved = True
    return solution

# GVNS algorithm
def GVNS(cities, k, max_restarts):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(max_restarts):
        initial_solution = generate_initial_solution(cities, k)
        current_solution = VND(initial_solution, cities)
        current_cost = calculate_total_cost(current_solution, cities)
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Define cities coordinates
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Parameters
k = 6  # Total cities to visit including the depot
max_restarts = 100  # Number of restarts for GVNS

# Solve the problem using GVNS
best_tour, min_cost = GVNS(cities, k, max_restarts)

# Output the best tour and the minimum travel cost found
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))