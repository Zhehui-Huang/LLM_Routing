import numpy as np
import random

# City coordinates
cities = [
    (90, 3),   # City 0: Depot
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Number of cities to visit (including the depot)
k = 6

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate a random initial solution of k cities including the depot
def generate_initial_solution():
    tour = [0] + random.sample(range(1, len(cities)), k-1)
    return tour[:k]

# Calculate the total distance of a tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += distance(cities[tour[i-1]], cities[tour[i]])
    total_distance += distance(cities[tour[-1]], cities[tour[0]])  # Return to depot
    return total_distance

# Perform shaking by swapping two cities in the tour
def shake(tour):
    shaken_tour = tour[:]
    idx1, idx2 = random.sample(range(1, k), 2)  # Avoid swapping the depot (index 0)
    shaken_tour[idx1], shaken_tour[idx2] = shaken_tour[idx2], shaken_tour[idx1]
    return shaken_tour

# Variable Neighborhood Descent for local optimization
def vnd(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, k):
            for j in range(i + 1, k):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if calculate_total_distance(new_tour) < calculate_total_distance(tour):
                    tour = new_tour
                    improved = True
    return tour

# GVNS algorithm
def gvns(max_iterations=100):
    best_solution = generate_initial_solution()
    best_distance = calculate_total_distance(best_solution)
    
    for _ in range(max_iterations):
        current_solution = shake(best_solution)
        improved_solution = vnd(current_solution)
        current_distance = calculate_total_distance(improved_solution)
        
        if current_distance < best_distance:
            best_solution = improved_solution
            best_distance = current_distance

    return best_solution, best_distance

# Running the GVNS algorithm
best_tour, best_cost = gvns(100)
final_tour = best_tour + [best_tour[0]]  # Adding the depot at the end for the full cycle round-trip

print("Tour:", final_tour)
print("Total travel cost:", best_cost)