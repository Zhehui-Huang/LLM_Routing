import numpy as np
import random
from itertools import permutations

# Coordinates of the cities
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Euclidean distance function
def distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Function to compute total travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate an initial feasible solution (random selection of k cities)
def generate_initial_solution(k):
    cities = list(range(1, len(coordinates)))  # city indices, excluding the depot
    random.shuffle(cities)
    selected_cities = cities[:k-1]  # Select k-1 cities, because we include the depot
    selected_cities.insert(0, 0)  # Start from the depot
    selected_cities.append(0)  # Return to the depot
    return selected_cities

# Local search swap procedure within a tour
def local_search(solution):
    best_cost = tour_cost(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = tour_cost(new_solution)
                    if new_cost < best_cost:
                        best_solution = new_solution[:]
                        best_cost = new_cost
                        improved = True
    return best_solution

# GVNS implementation
def gvns(k, max_iter=100, shake_strength=2):
    best_solution = generate_initial_solution(k)
    best_cost = tour_cost(best_solution)
    iter = 0
    
    while iter < max_iter:
        # Shake: generate a new solution from neighborhood
        shuffled_indices = list(range(1, k-1))
        random.shuffle(shuffled_indices)
        shuffled_indices = [0] + shuffled_indices + [0]
        current_solution = [best_solution[idx] for idx in shuffled_indices]
        current_cost = tour_cost(current_solution)
        
        # Variable Neighborhood Descent (Local Search)
        current_solution = local_search(current_solution)
        current_cost = tour_cost(current_solution)
        
        # Acceptance criterion
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
            
        iter += 1
    
    return best_solution, best_cost

# Number of cities to visit including the depot
k = 10

# Perform the GVNS
best_solution, best_cost = gvns(k)

# Output the results
print(f"Tour: {best_solution}")
print(f"Total travel cost: {best_cost:.2f}")