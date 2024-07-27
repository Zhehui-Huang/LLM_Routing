import math
import random

# City coordinates, including the depot city as the first element
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Distances based on euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate an initial feasible solution randomly
def generate_initial_solution(k=7):
    solution = [0]  # Start with the depot city
    while len(solution) < k:
        new_city = random.choice([i for i in range(1, len(cities)) if i not in solution])
        solution.append(new_city)
    solution.append(0)  # End at the depot city
    return solution

# Total cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return total_cost

# Shake function: Generate a random neighbor solution
def shake(solution, k=7):
    new_solution = solution[1:-1]
    random.shuffle(new_sol...
    while len(new_solution) + 2 != k:
        item_to_add = random.choice([i for i in range(1, len(cities)) if i not in new_solution])
        new_solution.append(item_to_add)
    return [0] + new_solution + [0]

# Local Search for Improvement
def local_search(solution):
    best_solution = solution
    best_cost = calculate_cost(solution)
    made_improvement = True
    
    while made_improvement:
        made_improvement = False
        for i in range(1, len(best_solution)-2):
            for j in range(i+1, len(best_solution)-1):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    made_improvement = True
    return best_solution

# GVNS Algorithm
def gvns(max_iter=100, k=7):
    current_solution = generate_initial_solution(k)
    best_solution = current_solution
    best_cost = calculate_cost(current_solution)
    
    for _ in range(max_iter):
        shaken_solution = shake(current_solution, k)
        new_solution = local_search(shaken_solution)
        new_cost = calculate_cost(new_solution)
        
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_cost
            # Reset since we found a better solution
            current_solution = new_solution
            
    return best_solution, best_cost

# Running the GVNS algorithm to find the best tour
best_tour, best_tour_cost = gvns(max_iter=1000, k=7)
print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))