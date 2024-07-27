import math
import random

# Define Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate Initial Solution
def generate_initial_solution(cities, k):
    solution = [0]  # Start at the depot city
    remaining_cities = cities[1:]  # Exclude the depot city initially
    while len(solution) < k:
        chosen_city = random.choice(remaining_cities)
        solution.append(cities.index(chosen_city))
        remaining_cities.remove(chosen_city)
    solution.append(0)  # End at the depot city
    return solution

# Calculate the total cost of the tour
def calculate_total_cost(solution, cities):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += euclidean_distance(cities[solution[i]], cities[solution[i+1]])
    return total_cost

# Shake function for GVNS
def shake(solution, k):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_solution[:k-2] + [0]

# Variable Neighborhood Descent (VND)
def VND(solution, cities):
    best_cost = calculate_total_cost(solution, cities)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if j != i:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = solution[j], solution[i]
                    new_cost = calculate_total_importance(new_solution, cities)
                    if new_cost < best_cost:
                        solution = new_solution
                        best_cost = new_cost
                        improved = True
    return solution

# Main GVNS function
def GVNS(cities, max_restarts, k):
    best_solution = None
    best_cost = float('inf')
    for _ in range(max_rests):
        initial_solution = generate_initial_solution(cities, k)
        current_solution = initial_solution[:]
        current_cost = calculate_total_cost(current_solution, cities)
        while True:
            shaken_solution = shake(current_solution, k)
            local_optimal_solution = VND(shaken_solution, cities)
            local_optimal_cost = calculate_total_cost(local_optimal_solution, cities)
            if local_optimal_cost < current_cost:
                current_solution = local_optimal_solution
                current_cost = local_optimal_cost
            else:
                break
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    return best_solution, best_cost

# Define cities as per problem statement
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Execute the GVNS algorithm
k = 6  # Including the depot
max_restarts = 50
best_tour, min_cost = GVNS(cities, max_restarts, k)
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))