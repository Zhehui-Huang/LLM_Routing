import random
import math

# Coordinates of cities including the depot
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def generate_initial_solution():
    selected_cities = random.sample(list(cities.keys())[1:], 7)  # Choose 7 random cities, excluding depot
    tour = [0] + selected_cities + [0]
    return tour

def shake(solution):
    # Swap two cities in the tour excluding the depot
    idx1, idx2 = random.sample(range(1, len(solution)-1), 2)
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

def calculate_total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def vnd(solution):
    best_solution = solution[:]
    best_cost = calculate_total_distance(best_solution)
    
    for i in range(1, len(solution) - 2):
        for j in range(i+1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_total_distance(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
    
    return best_solution

def gvns(k_max, num_restarts):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        solution = generate_initial_solution()
        cost = calculate_total_distance(solution)
        
        for _ in range(k_max):
            solution = shake(solution)
            solution = vnd(solution)
            cost = calculate_total_distance(solution)
            
            if cost < best_cost:
                best_solution = solution
                best_cost = cost
                
    return best_solution, best_cost

# Parameters for GVNS
k_max = 10
num_restarts = 50

# Finding the best tour
best_tour, best_total_cost = gvns(k_max, num_restarts)

print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)