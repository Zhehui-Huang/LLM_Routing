import numpy as np
import random

# Define the positions of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = distance(i, j)

# Algorithm subroutines
def generate_initial_solution(V):
    initial_cities = [0]
    remaining_cities = set(V) - set(initial_cities)
    while len(initial_cities) < 5:
        new_city = random.choice(list(remaining_cities))
        initial_cities.append(new_city)
        remaining_cities.remove(new_city)
    initial_cities.append(0)  # Ensure to return to the starting city
    return initial_cities

def calculate_total_distance(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def shake(solution):
    inner_cities = solution[1:-1]  # Avoid the depot city
    random.shuffle(inner_cities)
    return [solution[0]] + inner_cities + [solution[0]]

def vnd(solution):
    best_solution = solution
    best_cost = calculate_total_distance(solution)
    
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                candidate = solution[:]
                candidate[i], candidate[j] = candidate[j], candidate[i]
                cost = calculate_total_distance(candidate)
                if cost < best_cost:
                    best_solution, best_cost = candidate, cost
                    improved = True
        solution = best_solution
        
    return best_solution

# GVNS algorithm implementation
def gvns(Nrst):
    S_best = generate_initial_solution(range(num_cities))
    best_cost = calculate_total_distance(S_best)
    
    for _ in range(Nrst):
        S = generate_initial_solution(range(num_cities))
        S = vnd(S)  # Immediate improvement before shaking for better start
        while True:
            S_prime = shake(S)
            S_double_prime = vnd(S_prime)
            cost_double_prime = calculate_total_distance(S_double_prime)
            
            if cost_double_prime < best_cost:
                S, best_cost = S_double_prime, cost_double_packet:
                break
            
        if best_cost < calculate_total_distance(S_best):
            S_best = S[:]
            
    return S_best, best_cost

# Set the number of restarts
Nrst = 100
best_tour, best_cost = gvns(Nrst)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)