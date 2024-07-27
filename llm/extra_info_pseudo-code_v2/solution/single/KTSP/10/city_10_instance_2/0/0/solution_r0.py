import random
import math
from itertools import permutations

# Locations of cities including the depot
coordinates = [
    (90, 3),   # Depot city 0
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def total_tour_cost(tour):
    """Calculate the total cost of the tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

def generate_initial_solution(k):
    """Generate a random initial solution that includes the depot."""
    cities = list(range(1, len(coordinates)))  # City indices excluding depot
    random.shuffle(cities)
    tour = [0] + cities[:k-2] + [0]  # Start and end at the depot
    return tour

def local_search(solution):
    """Apply simple local search by trying to swap two cities and check if it improves the solution."""
    best_cost = total_tour_cost(solution)
    best_solution = solution[:]
    made_improvement = False

    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = total_tour_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution
                made_improvement = True
    return best_solution, made_improvement

def gvns(k, max_iter=100):
    """General Variable Neighborhood Search."""
    current_solution = generate_initial_solution(k)
    best_solution = current_solution[:]
    best_cost = total_tour_cost(current_solution)
    
    iteration = 0
    while iteration < max_iter:
        new_solution = generate_initial_solution(k)
        for _ in range(10):  # Perform local search multiple rounds
            new_solution, improved = local_search(new_solution)
            if improved:
                new_cost = total_tour_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
        iteration += 1

    return best_solution, best_cost

# Set the number of cities to visit including the depot.
k = 6

# Find and print the best tour and its cost.
best_solution, best_cost = gvns(k)
print("Tour:", best_solution)
print("Total travel cost:", round(best_cost, 2))