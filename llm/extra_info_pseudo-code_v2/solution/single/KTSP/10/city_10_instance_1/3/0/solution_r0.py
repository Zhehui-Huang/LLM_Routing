import numpy as np
import random
from itertools import permutations

# Locations of cities including the depot city
locations = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((locations[city1][0] - locations[city2][0])**2 + (locations[city1][1] - locations[city2][1])**2)

# Generate an initial solution: start at depot, select 4 random other cities
def generate_initial_solution():
    cities = list(range(1, len(locations)))  # All cities except depot
    random.shuffle(cities)
    tour = [0] + cities[:4] + [0]
    return tour

# Calculate total travel cost for the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Shake: Generate a neighbor solution by swapping two random cities in the tour
def shake(tour):
    idx1, idx2 = np.random.randint(1, 5), np.random.randint(1, 5)
    new_tour = tour[:]
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return new_tour

# Local Search (First Improvement Strategy): try improving the tour by exchanging cities
def local_search(tour):
    best_cost = tour_cost(tour)
    best_tour = tour[:]
    improved = False
    
    for i in range(1, 5):
        for j in range(i+1, 5):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = tour_cost(new_tour)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour
                improved = True
                break
        if improved:
            break

    return best_tour

# Variable neighborhood descent
def VND(tour):
    local_opt = tour[:]
    improved = True
    while improved:
        new_tour = local_search(local_opt)
        if tour_cost(new_tour) < tour_cost(local_opt):
            local_opt = new_values[:]
        else:
        return new_tour

# General Variable Neighborhood Search
def GVNS(max_iter=100):
    best_tour = generate_initial_solution()
    best_cost = tour_cost(best_tour)
    
    for _ in range(max_iter):
        current_tour = best_tour[:]
        current_tour = shake(current_tour)
        current_tour = VND(current_tour)
        current_cost = tour_cost(current_tour)
        
        if current_cost < best_cost:
            best_tour = current_tour[:]
            best_cost = current_cost
    
    return best_tour, best_cost

# Execute the algorithm
final_tour, final_cost = GVNS(max_iter=200)
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")