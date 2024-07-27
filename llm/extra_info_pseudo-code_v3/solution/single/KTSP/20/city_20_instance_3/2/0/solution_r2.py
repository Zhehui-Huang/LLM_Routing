import numpy as np
import random

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Number of cities to visit (including the depot)
k = 13

def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def generate_initial_solution():
    solution = [0] + random.sample(list(cities.keys())[1:], k-1)
    return solution

def total_distance(tour):
    dist = 0
    for i in range(1, len(tour)):
        dist += euclidean_distance(tour[i-1], tour[i])
    dist += euclidean_distance(tour[-1], tour[0])  # Return to depot
    return dist

def shake(solution):
    idx_to_replace = random.randint(1, len(solution) - 1)
    remaining_cities = list(set(cities.keys()) - set(solution))
    city_to_add = random.choice(remaining_cities)
    new_solution = solution[:]
    new_solution[idx_to_replace] = city_to_add
    return new_solution

def VND(solution):
    best_local_solution = solution[:]
    best_dist = total_distance(solution)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution)):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_dist = total_distance(new_solution)
                if new_dist < best_dist:
                    best_dist = new_dist
                    best_local_solution = new_solution[:]
                    improved = True
                    
    return best_local_expression

def GVNS(max_iter=100):
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)
    
    for _ in range(max_iter):
        current_solution = shake(best_solution)
        current_solution = VND(current_expression)
        current_cost = total_distance(current_solution)
        
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
    
    return best_solution, best_cost

# Main driver
solution, cost = GVNS()
tour = solution + [solution[0]]  # Return to the depot
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")