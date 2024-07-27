import math
import random

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def generate_initial_solution(k=7):
    solution = [0]  # Start at the depot city
    available_cities = list(range(1, len(cities)))
    while len(solution) < k:
        new_city = random.choice(available_cities)
        solution.append(new_city)
        available_cities.remove(new_city)
    solution.append(0)  # Return to the depot city
    return solution

def calculate_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def shake(solution, k=7):
    base_solution = solution[1:-1]
    random.shuffle(base_solution)
    return [0] + base_solution[:k-2] + [0]

def local_search(solution):
    best_solution = solution[:]
    best_cost = calculate_cost(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i + 1, len(best_solution) - 1):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new_cost
                    improved = True
    return best_solution

def gvns(max_iter=500, k=7):
    current_solution = generate_initial_solution(k)
    best_solution = current_solution[:]
    best_cost = calculate_cost(current_solution)
    
    for _ in range(max_iter):
        current_solution = shake(best_solution, k)
        new_solution = local_search(current_solution)
        new_cost = calculate_cost(new_solution)
        if new_cost < best_cost:
            best_solution, best_cost = new_solution[:], new_cost
    return best_solution, best_cost

# Running the GVNS algorithm to find the solution
best_tour, best_tour_cost = gvns(max_iter=1000, k=7)
print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))