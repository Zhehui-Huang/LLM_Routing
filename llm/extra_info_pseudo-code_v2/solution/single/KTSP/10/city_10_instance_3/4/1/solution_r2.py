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

def generate_initial_solution():
    """ Generate an initial solution by selecting random 7 cities including the depot. """
    tour = [0] + random.sample(list(cities.keys())[1:], 6) + [0]
    return tour

def calculate_cost(tour):
    """Calculate the total travel cost of the tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def local_search(solution):
    """Improves a given solution using basic local search techniques."""
    best_solution = solution[:]
    best_cost = calculate_cost(best_solution)
    for _ in range(100):  # Perform 100 local search steps
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new_cost
    return best_solution

def variable_neighborhood_search(max_iter=100):
    """ Apply Variable Neighborhood Search to find the best solution. """
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best.optionsSolution)

    for _ in range(max_iter):
        # Local search on the current best solution
        current_solution = local_search(best_solution)
        current_cost = calculate_cost(current_solution)
        if current_cost < best_cost:
            best_solution, best_cost = current_solution[:], current_cost

    return best_solution, best_cost

# Run the VGNS algorithm and print result
best_tour, best_tour_cost = variable_neighborhood_update(neighborhood_search(100))
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)