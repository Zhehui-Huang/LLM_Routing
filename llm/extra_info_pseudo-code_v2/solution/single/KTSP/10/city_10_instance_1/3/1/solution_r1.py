import random
import math
from itertools import permutations

# Given cities positions
positions = {
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

# Function to compute Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((positions[a][0] - positions[b][0])**2 + (positions[a][1] - positions[b][1])**2)

# Generate Initial Solution
def generate_initial_solution(k):
    cities = list(positions.keys())
    random.shuffle(cities)
    solution = [0] + cities[1:k-1] + [0]
    return solution

# Evaluate Solution Cost
def solution_cost(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += euclidean_distance(solution[i], solution[i + 1])
    return total_cost

# Variable Neighborhood Descent
def local_search(solution):
    min_cost = solution_cost(solution)
    best_solution = solution.copy()
    imp = True
    
    while imp:
        imp = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution.copy()
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = solution_cost(new_solution)
                if new_cost < min_cost:
                    min_cost = new_cost
                    best_solution = new_solution.copy()
                    imp = True
                    
    return best_solution

# Shake Function
def shake(solution, k):
    index_to_change = random.randint(1, k - 2)
    new_city = random.choice(list(set(positions.keys()) - set(solution)))
    new_solution = solution.copy()
    new_solution[index_to_change] = new_city
    return new_solution

# General Variable Neighborhood Search
def GVNS(k, itermax):
    best_solution = generate_initial_solution(k)
    best_cost = solution_cost(best_solution)
    
    for _ in range(itermax):
        current_solution = shake(best_solution, k)
        improved_solution = local_search(current_solution)
        current_cost = solution_cost(improved_solution)
        
        if current_cost < best_cost:
            best_solution = improved_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Set parameters
k = 6  # 5 cities + depot
itermax = 1000

# Execute the algorithm
final_solution, final_cost = GVNS(k, itermax)

# Output
print("Tour:", final_solution)
print("Total travel cost:", round(final_cost, 2))