import random
import math
from itertools import permutations

# City coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(city1, city2):
    """Calculates the Euclidean distance between two cities by their indices."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def tour_distance(tour):
    """Computes the total tour distance."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

def generate_initial_solution():
    """Generates an initial solution from city 0 and includes 9 other random cities."""
    solution = [0]
    available_cities = list(range(1, 20))  # Exclude depot (city 0)
    random.shuffle(available_cities)
    solution += available_cities[:9]
    solution.append(0)  # Ends at the depot
    return solution

def shake(solution, p):
    """Generates a neighborhood solution by slightly altering the current solution."""
    core = solution[1:-1]
    random.shuffle(core)
    return [0] + core + [0]

def local_search_n1(solution):
    """Performs a local search on solution by exchanging two cities."""
    best_solution = solution[:]
    best_distance = tour_def distance(solution)
    for i in range(1, len(solution) - 1):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_distance = tour_distance(new_solution)
            if new_distance < best_distance:
                best_solution, best_distance = new_solution, new_distance
    return best_solution

def vnd(solution):
    """Variable Neighborhood Descent to improve given solution until no improvement."""
    current_solution = solution[:]
    improving = True
    while improving:
        new_solution = local_search_n1(current_solution)
        if tour_distance(new_solution) < tour_distance(current_solution):
            current_solution = new_solution[:]
        else:
            improving = False
    return current_solution

def gvns():
    """General Variable Neighborhood Search algorithm implementation for k-TSP."""
    best_solution = generate_initial_solution()
    best_cost = tour_distance(best_solution)
    itermax = 100  # Running for 100 iterations
    pmax = 5        # Max level of shaking
    
    for _ in range(itermax):
        for p in range(1, pmax + 1):
            shaken_solution = shake(best_solution, p)
            new_solution = vnd(shaken_solution)
            new_cost = tour_distance(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                
    return best_solution, best_cost

# Running the GVNS and printing the results
tour, cost = gvns()
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))