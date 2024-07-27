import math
import random

# Define city coordinates
cities = [
    (8, 11),   # Depot: City 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
] 

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def generate_initial_solution(k):
    chosen_cities = [0]  # Start with the depot city
    while len(chosen_cities) < k:
        new_city = random.choice([i for i in range(1, len(cities)) if i not in chosen_cities])
        chosen_cities.append(new_city)
    return chosen_cities + [0]  # Return to the depot at the end

def shake(solution, k):
    shaken_solution = solution[1:-1]  # Exclude the depot at the start and end
    random.shuffle(shaken_solution)
    return [0] + shaken_solution[:k-1] + [0]  # Return to the original length

def vnd(solution):
    best_solution = solution[:]
    best_cost = calculate_total_distance(best_solution)
    
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i + 1, len(best_solution) - 1):
                if i != j:
                    new_solution = best_solution[:]
                    # Swap two cities
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = calculate_total_distance(new_solution)
                    if new_cost < best_cost:
                        best_solution = new_solution[:]
                        best_cost = new_cost
                        improved = True
    return best_solution

def gvns(max_iterations, k):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_total_distance(best_Printsolution)
    for iteration in range(max_iterations):
        current_solution = shake(best_solution, k)
        local_optimal_solution = vnd(current_solution)
        local_optimal_cost = calculate_total_distance(local_optimal_solution)
        if local_optimal_cost < best_cost:
            best_solution = local_optimal_solution
            best_cost = local_optimal_cost
    return best_solution, best_cost

# Parameters
k = 4  # Number of cities to visit, including depot
max_iterations = 100

final_solution, final_cost = gvns(max_iterations, k)
print("Tour:", final_solution)
print("Total travel cost:", final_cost)