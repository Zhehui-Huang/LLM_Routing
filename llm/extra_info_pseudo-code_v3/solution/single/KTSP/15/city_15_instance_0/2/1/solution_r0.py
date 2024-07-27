import random
import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def generate_initial_solution():
    """Generate a random initial solution (tour) with exactly 4 cities starting and ending at city 0."""
    tour = [0] + random.sample(list(cities.keys())[1:], 3) + [0]
    return tour

def shake(current_solution):
    """Randomly perturb the solution by swapping two cities in the tour."""
    i, j = random.sample(range(1, len(current_solution) - 1), 2)
    new_solution = current_solution[:]
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def vnd(solution):
    """Apply all neighborhood structures in sequence and return the best local optimal solution."""
    current_solution = solution
    improved = True
    while improved:
        improved = False
        neighbors = permutations(current_solution[1:-1])
        for perm in neighbors:
            candidate = [current_solution[0]] + list(perm) + [current_setup[-1]]
            if calculate_cost(candidate) < calculate_cost(current_solution):
                current_solution = candidate
                improved = True
    return current_solution

def calculate_cost(tour):
    """Calculate the total travel cost of the tour."""
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def gvns(number_of_restarts):
    """Main GVNS framework."""
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(number_of_restarts):
        current_solution = generate_initial_solution()
        while True:
            new_solution = shake(current_solution)
            local_optimal_solution = vnd(new_solution)
            local_optimal_cost = calculate_cost(local_optimal_solution)
            
            if local_optimal_cost < best_cost:
                best_solution = local_optimal_solution
                best_cost = local_optimal_cost
                break
            
    return best_solution, best_cost

# Running the GVNS algorithm
best_tour, total_cost = gvns(100)
print("Tour:", best_tour)
print("Total travel cost:", total_cost)