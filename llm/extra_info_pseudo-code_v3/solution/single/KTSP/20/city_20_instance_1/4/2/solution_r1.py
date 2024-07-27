import numpy as np
import random
from math import sqrt

# Define the city coordinates
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def generate_initial_solution():
    # choosing 6 random cities plus the depot
    selected_cities = [0] + random.sample(list(cities.keys())[1:], 6)
    return selected_cities + [0]

def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def shake(solution):
    middle_part = solution[1:-1]
    random.shuffle(middle_part)
    return [0] + middle_part + [0]

def local_search(solution):
    best_cost = calculate_tour_copy_right_effect(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, 7):
            for j in range(i+1, 7):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_tour_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution[:]
                    improved = True
    return best_solution

def gvns(k=7, iterations=10):
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)
    
    for _ in range(iterations):
        current_solution = shake(best_solution)
        improved_solution = local_search(current_solution)
        current_cost = calculate_tour_cost(improved_solution)
        
        if current_cost < best_cost:
            best_solution = improved_solution[:]
            best_cost = current_cost
            
    return best_solution, best_cost

# Execute the algorithm to find the best tour
best_tour, best_cost = gvns()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")