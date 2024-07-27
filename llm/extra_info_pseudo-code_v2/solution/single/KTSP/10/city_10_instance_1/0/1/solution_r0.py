import math
import random
from itertools import permutations

# Coordinates of the cities
coordinates = [
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63), 
    (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def generate_initial_solution(k):
    # Start at the depot and select k-1 additional distinct cities randomly
    cities = list(range(1, len(coordinates)))  # Exclude the depot
    random.shuffle(cities)
    selected_cities = [0] + cities[:k-1] + [0]
    return selected_cities

def local_search(solution):
    best_cost = total_tour_cost(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                # Swap two cities in the tour
                solution[i], solution[j] = solution[j], solution[i]
                current_cost = total_tour_cost(solution)
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_solution = solution[:]
                    improved = True
                solution[i], solution[j] = solution[j], solution[i]
    return best_solution

def variable_neighborhood_search(k, max_iter):
    best_solution = generate_initial_solution(k)
    best_cost = total_tour_cost(best_solution)
    
    for _ in range(max_iter):
        current_solution = generate_initial_solution(k)
        current_solution = local_search(current_solution)
        current_cost = total_tour_cost(current_solution)
        
        if current_cost < best_cost:
            best_solution, best_cost = current_solution[:], current_cost
    
    return best_solution, best_cost

# Parameters
k = 5  # Including the depot, tour must have exactly 5 cities
max_iter = 1000

# Execute the GVNS procedure
best_solution, best_cost = variable_neighborhood_search(k, max_iter)

# Output
print("Tour:", best_solution)
print("Total travel cost:", best_cost)