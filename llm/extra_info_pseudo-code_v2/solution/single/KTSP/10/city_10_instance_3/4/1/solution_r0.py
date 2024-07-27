import random
import math
from itertools import permutations

# Fixed seed for reproducibility
random.seed(42)

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

def generate_initial_solution():
    """Generate an initial solution with random 7 cities starting and ending with depot (city 0)."""
    selected_cities = [0] + random.sample(list(cities.keys())[1:], 6) + [0]
    return selected_cities

def calculate_cost(tour):
    """Calculate the total travel cost of the tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def local_search(solution):
    """Perform local search by trying permutations of the intermediate cities."""
    best_solution = solution[:]
    best_cost = calculate_cost(best_solution)
    for i in range(1, 6):
        for j in range(i+1, 7):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new
    
    return best_solution

def variable_neighborhood_search(max_iter):
    """Perform the GVNS to find the best solution."""
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_cost)
    
    for _ in range(max_iter):
        current_solution = generate_initial_solution()
        for pmax in [100, 200]:  # Different neighborhood size definitions arbitrarily set
            for _ in range(pmax):
                new_solution = local_search(current_solution)
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    break
    return best_solution, best_cost

# Set maximum iterations
max_iterations = 1000
best_solution, best_cost = variable_neighborhood_search(max_iterations)

print("Tour:", best_solution)
print("Total travel cost:", best_cost)