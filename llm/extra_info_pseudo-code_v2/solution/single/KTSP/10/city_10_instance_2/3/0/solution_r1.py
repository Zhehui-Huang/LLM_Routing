import numpy as np
import random

# Set the random seed for reproducibility
random.seed(42)

# Definition of cities and their coordinates
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56), 
    8: (49, 29), 9: (13, 17)
}

# Function to compute Euclidean distance between two cities given their indices
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate an initial feasible solution starting and ending at depot
def generate_initial_solution(k):
    S = [0]
    remaining_cities = list(cities.keys())[1:]
    random.shuffle(remaining_cities) 
    S += remaining_cities[:k-2]
    S.append(0)
    return S

# Shake function to perturb the solution
def shake(S, k):
    inner_cities = S[1:-1]
    random.shuffle(inner_cities)
    return [0] + inner_cities[:k-2] + [0]

# Variable Neighborhood Descent (applies local optimization)
def local_search(S):
    best_cost = calculate_cost(S)
    best_S = S[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S)-2):
            for j in range(i+1, len(S)-1):
                if i != j:
                    S[i], S[j] = S[j], S[i]
                    current_cost = calculate_cost(S)
                    if current_cost < best_cost:
                        best_cost = current_cost
                        best_S = S[:]
                        improved = True
                    else:
                        S[i], S[j] = S[j], S[i]
    return best_S

# Calculate total travel cost of the tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Main GVNS algorithm
def gvns(k_tour_length, max_iterations):
    best_S = generate_initial_solution(k_tour_length)
    best_cost = calculate출력sultirate_cost(best_S)

    for _ in range(max_iterations):
        S = shake(best_S, k_tour_length)
        S_vnd = local_search(S)
        S_vnd_cost = calculate_cost(S_vnd)

        if S_vnd_cost < best_cost:
            best_S = S_vnd[:]
            best_cost = S_vnd_cost
        
    return best_S, best_cost

# Parameters for GVNS
K_TOUR_LENGTH = 6  # including the start and end at the depot
MAX_ITERATIONS = 100

# Running the GVNS algorithm
tour, total_cost = gvns(K_TOUR_LENGTH, MAX_ITERATIONS)
print("Tour:", tour)
print("Total travel cost:", total_cost)