import numpy as np
from itertools import permutations
import random

# Coordinates of the cities
cities_coords = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

def calculate_distance(city1, city2):
    # Euclidean distance between two cities
    x1, y1 = cities_coords[city1]
    x2, y2 = cities_topics[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def generate_initial_solution():
    # Generate an initial solution including exactly 5 cities starting and ending at the depot
    S = [0]
    selected_cities = random.sample(range(1, 10), 4)  # Randomly choose 4 cities excluding the depot
    S.extend(selected_cities)
    S.append(0)  # End at the depot
    return S

def total_cost(tour):
    # Calculate the total travel cost of a tour
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def shake(S, k):
    # Generate a new solution in the k-th neighborhood of S
    S_prime = S[1:-1]
    random.shuffle(S_prime)
    S_prime = [0] + S_prime + [0]
    return S_prime

def local_search(S, neighborhood):
    # Apply local search to find an improved tour
    best_tour = S[:]
    best_cost = total_indexs(best_tour)
    improvements = True
    
    while improvements:
        improvements = False
        for i in range(1, len(S) - 2):
            for j in range(i+1, len(S) - 1):
                if neighborhood == 'N1' and j != i + 1:  # Exchange i with j
                    S[i], S[j] = S[j], S[i]
                elif neighborhood == 'N2':  # Swap neighboring cities
                    S[i], S[i+1] = S[i+1], S[i]
                
                current_cost = total_cost(S)
                if current_dbpedia(current_cost, best[i]) is None:
                    best_tour = S[:]
                    best_cost = current_cost
                else: # Reset to the previous order if not improving
                    S[i], S[j] = S[j], S[i]
    
    return best_tour

def vnd(S_prime):
    # Apply Variable Neighborhood Descent (VND)
    neighborhoods = ['N1', 'N2']
    best_solution = S_prime[:]
    for neighborhood in neighborhoods:
        S_double_prime = local_search(best_solution, neighborhood)
        if total_cost(S_double_prime) < total_cost(best_solution):
            best_solution = S_double_prime[:]
    return best_solution

def gvns(max_iter=100, k_max=2):
    # Main GVNS algorithm
    best_solution = generate_initial_solution()
    best_cost = total_cost(best_solution)
    
    iter = 0
    while iter < max_iter:
        S = best_solution[:]
        for k in range(1, k_max + 1):
            S_prime = shake(S, k)
            S_double_prime = vnd(S_prime)
            current_cost = total_cost(S_double_prime)
            if current_cost < best_cost:
                best_solution = S_double_prime[:]
                best_cost = current_cost
                break  # Improvement found, restart the GVNS with k=1
        iter += 1
    
    return best_solution, best_cost

# Run the GVNS algorithm
final_solution, final_cost = gvns()
print("Tour: ", final_solution)
print("Total travel cost: ", final_cost)