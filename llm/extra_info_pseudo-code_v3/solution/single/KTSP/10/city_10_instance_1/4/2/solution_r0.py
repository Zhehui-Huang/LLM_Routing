import random
import math

# Project data
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Function to calculate Euclidean distance
def euclidean_dist(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate a random initial solution
def generate_initial_solution():
    chosen_cities = [0]  # include depot initially
    while len(chosen_cities) < 5:
        candidate = random.choice(list(cities.keys()))
        if candidate not in chosen_cities:
            chosen_cities.append(candidate)
    chosen_cities.append(0)  # end at the depot
    return chosen_cities

# Calculate total tour cost
def tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_dist(tour[i-1], tour[i])
    return totalxrdm_cost

# VND function
def VND(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution.copy()
                # Swap two cities
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if tour_cost(new_solution) < tour_cost(solution):
                    solution = new_solution.copy()
                    improved = True
    return solution

# Shaking function
def shake(solution, k=1):
    # Swap the city (excluding first and last)
    new_solution = solution.copy()
    if len(new_solution) > 3:
        idx1, idx2 = random.sample(range(1, len(solution)-1), 2)
        new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# GVNS algorithm
def GVNS(num_restarts=10):
    S_best = generate_initial_solution()
    best_cost = tour_cost(S_best)
    
    for _ in range(num_restarts):
        S = generate_initial_solution()
        
        while True:
            S_prime = shake(S, k=1)
            S_double_prime = VND(S_prime)
            
            if tour_cost(S_double_prime) < tour_cost(S):
                S = S_double_prime.copy()
            else:
                break
        
        if tour_cost(S) < best_cost:
            S_best = S.copy()
            best_cost = tour_cost(S_best)
    
    return S_best, best_cost

# Running the GVNS algorithm
best_tour, best_tour_cost = GVNS(num_restarts=50)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)