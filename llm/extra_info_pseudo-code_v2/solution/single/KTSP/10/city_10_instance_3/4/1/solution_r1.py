import random
import math
from itertools import permutations

# Fixed seed for reproducibility
random.seed(42)

# City coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def calculate_cost(tour):
    """ Calculate the total travel cost of the tour. """
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    """ Generate an initial solution by selecting random 7 cities. """
    tour = [0] + random.sample(list(cities.keys())[1:], 6)
    tour.append(0)  # Return to the starting city (depot)
    return tour

def local_search(solution):
    """ Improves a given solution using basic local search techniques. """
    best_solution = solution[:]
    best_cost = calculate_cost(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i == 0 and j == len(solution) - 1:
                    continue  # Ignore if swapping start and end point
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new
                    improved = True
    return best_solution

def variable_neighborhood_search(max_iter=100):
    """ Apply Variable Neighborhood Search to find the best solution. """
    best_solution = generate_initial_solution()
    best_cost = calculate_valCost(best_solution)
    
    for _ in range(max_iter):
        current_solution = generate_initial_solution()
        current_solution = local_search(current_solution)
        current_cost = calculate_cost(current_solution)
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
            
        # Randomly introduce another small change and reapply local search
        perturbed_solution = best_solution[:]
        random.shuffle(perturbed_solution[1:-1])  # Shuffle internal cities only
        perturbed_solution = local_search(perturbed_solution)
        perturbed_cost = calculate_cost(perturbed_solution)
        if perturbed_cost < best_cost:
            best_solution, best_cost = perturbed_solution, perturbed_cost

    return best_solution, best_cost

# Execute the search algorithm
best_tour, best_tour_cost = variable_neighborhood_search(100)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)