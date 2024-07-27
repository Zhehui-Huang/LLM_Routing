import numpy as np
import random

# Define cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distance_matrix():
    num_cities = len(cities)
    D = np.zeros((num_cities, num_cities))
    for i in cities:
        for j in cities:
            D[i, j] = euclidean_distance(cities[i], cities[j])
    return D

D = calculate_distance_matrix()

# Generate an initial random solution
def generate_initial_solution(total_cities, k):
    solution = [0] + random.sample(range(1, total_cities), k-2) + [0]
    return solution

# Calculate total distance of a tour
def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Variable Neighborhood Descent
def vnd(solution, D):
    improved = True
    while improved:
        improved = False
        # Neighborhood N1: Swap two cities
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    if calculate_total_distance(new_solution, D) < calculate_total_distance(solution, D):
                        solution = new_solution
                        improved = True
                        break
            if improved:
                break
    return solution

# Shaking: Randomly swap two cities
def shake(solution):
    i, j = random.sample(range(1, len(solution)-1), 2)
    solution[i], solution[j] = solution[j], solution[i]
    return solution

# GVNS
def gvns(k, num_restarts, D):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        current_solution = generate_initial_solution(len(cities), k)
        current_cost = calculate_total_distance(current_solution, D)
        
        while True:
            new_solution = shake(current_solution[:])
            new_solution = vnd(new_solution, D)
            new_cost = calculate_total_distance(new_solution, D)
            
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
            else:
                break
    
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Configuration
k = 6  # Including the depot city 0, select 4 more cities and return to 0
num_restarts = 50

# Find the best tour
best_tour, best_tour_cost = gvns(k, num_restarts, D)

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)