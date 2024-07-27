import numpy as al
import math
from random import randint, shuffle

# Calculate Euclidean distance between two coordinates
def euclidean_distance(c1, c2):
    return math.hypot(c1[0] - c2[0], c1[1] - c2[1])

# Define the coordinates for the cities
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Define the number of cities to visit including the depot
k = 4  

# Generate initial solution S
def generate_initial_solution():
    solution = [0]
    available_cities = list(range(1, len(cities)))
    shuffle(available_cities)
    while len(solution) < k:
        next_city = available_cities.pop()
        solution.append(next_city)
    solution.append(0)  # Returning to the depot
    return solution

# Calculate the total cost of the tour
def calculate_cost(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += euclidean_distance(cities[solution[i]], cities[solution[i+1]])
    return total_cost

# Perform local search on a given solution
def local_search(solution):
    best_cost = calculate_cost(solution)
    best_solution = solution.copy()
    improved = True
    while improved:
        improved = False
        for i in range(1, k-1):
            for j in range(i+1, k):
                # Trying swapping two cities
                new_solution = solution.copy()
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution.copy()
                    improved = True
    return best_solution

# Run GVNS
def gvns(max_iterations=100):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    for _ in range(max_iterations):
        current_solution = generate_initial_solution()
        current_solution = local_search(current_solution)
        current_cost = calculate_cost(current_solution)
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    return best_solution, best_cost

# Execute the algorithm
final_solution, final_cost = gvns()
print("Tour:", final_solution)
print("Total travel cost:", final_cost)