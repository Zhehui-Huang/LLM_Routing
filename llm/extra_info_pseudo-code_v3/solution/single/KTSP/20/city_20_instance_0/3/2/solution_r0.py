import numpy as np
import random

# Coordinates of cities
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def generate_initial_solution():
    available_cities = list(cities.keys())[1:]  # Exclude depot city from random selection
    selected_cities = random.sample(available_cities, 3)
    return [0] + selected_cities + [0]

def shake(solution):
    intermediate = solution[1:-1]
    random.shuffle(intermediate)
    return [0] + intermediate + [0]

def vnd(solution, n1=20, n2=20):
    current_solution = solution[:]
    improved = True
    
    while improved:
        improved = False
        for _ in range(n1):
            # Try swapping neighboring cities
            for i in range(1, len(current_solution) - 2):
                for j in range(i + 1, len(current_solution) - 1):
                    new_solution = current_solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    if calculate_total_distance(new_solution) < calculate_total_distance(current_solution):
                        current_solution = new_solution
                        improved = True

    return current_solution

def gvns(nrst=100):
    best_solution = generate_initial_tools()
    best_distance = calculate_total_distance(best_solution)
    
    for _ in range(nrst):
        current_solution = generate_initial_solution()
        current_solution = vnd(current_solution)
        
        while True:
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_distance = calculate_total_distance(new_solution)
            
            if new_distance < best_distance:
                best_solution = new_solution
                best_distance = new_distance
                break
            else:
                break
            
    return best_solution, best_distance

# Running the algorithm
optimal_tour, optimal_cost = gvns(nrst=100)
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))