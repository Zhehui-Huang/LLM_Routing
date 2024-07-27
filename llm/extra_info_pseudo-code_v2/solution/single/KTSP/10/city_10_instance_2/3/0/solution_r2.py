import numpy as np
import random

# Set random seed for reproducibility
random.seed(42)

# Cities and their coordinates
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56), 
    8: (49, 29), 9: (13, 17)
}

# Compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate the total travel cost of a tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate a random initial solution
def generate_initial_solution(k):
    initial_cities = list(cities.keys())
    random.shuffle(initial_cities)
    initial_solution = [0] + initial_cities[1:k-1] + [0]
    return initial_solution

# Shake the solution within the neighborhood
def shake(S, k):
    inner_cities = S[1:-1]
    random.shuffle(inner_cities)
    return [0] + inner_cities + [0]

# Local search for improvement
def local_search(S):
    best_cost = calculate_cost(S)
    best_solution = S[:]
    for i in range(1, len(S)-2):
        for j in range(i+1, len(S)-1):
            new_solution = S[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    return best_solution

# Variable Neighborhood Descent
def vnd(S):
    return local_search(S)

# General Variable Neighborhood Search (GVNS)
def gvns(k_tour_length, max_iterations):
    current_solution = generate_initial_solution(k_tour_length)
    best_solution = current_solution[:]
    best_cost = calculate_cost(current_solution)

    for _ in range(max_iterations):
        S = shake(current_solution, k_tour_length)
        S = vnd(S)
        cost = calculate_cost(S)
        if cost < best_cost:
            best_solution = S[:]
            best_cost = cost

    return best_solution, best_cost

# Set parameters for the problem
K_TOUR_LENGTH = 6  # Number of cities including start/end at the depot
MAX_ITERATIONS = 1000  # Number of iterations to perform

# Execute the GVNS algorithm
tour, total_cost = gvns(K_TOUR_LENGTH, MAX_ITERATIONS)
print("Tour:", tour)
print("Total travel cost:", total_cost)