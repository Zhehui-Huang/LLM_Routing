import random
import math
from itertools import permutations

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Euclidean distance calculation
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate total distance of the tour
def tour_distance(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate a random initial solution of k cities
def generate_initial_solution(k):
    selected_cities = [0]  # Start at the depot
    while len(selected_cities) < k:
        new_city = random.choice(list(set(cities.keys()) - set(selected_cities)))
        selected_cities.append(new_city)
    selected_cities.append(0)  # End at the depot
    return selected_cities

# Local search operators
def local_search(solution):
    best_solution = solution.copy()
    best_cost = tour_distance(best_solution)
    
    # Try all pairs of non-depot exchanges
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution.copy()
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = tour_distance(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
    
    return best_solution

# GVNS
def gvns(max_iter=1000, k=7):
    best_solution = generate_initial_solution(k)
    best_cost = tour_distribution(best_solution)
    
    for _ in range(max_iter):
        new_solution = generate_initial_solution(k)
        new_solution = local_search(new_solution)
        new_solution_cost = tour_distance(new_solution)
        if new_solution_cost < best_cost:
            best_solution = new_solution
            best_cost = new_solution_cost
            
    return best_solution, best_cost

# Finding the solution
best_tour, best_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)