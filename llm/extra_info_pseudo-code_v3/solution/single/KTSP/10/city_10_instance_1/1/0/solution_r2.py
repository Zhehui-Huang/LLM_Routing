import math
import random

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i + 1]]
    return total_cost

def shake(solution, distance_matrix):
    i = random.randint(1, len(solution) - 3)
    j = random.randint(1, len(solution) - 2)
    if i != j:
        solution[i], solution[j] = solution[j], solution[i]
    return solution

def variable_neighborhood_descent(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_tour_cost(new_solution, distance_matrix) < calculate_tour_cost(solution, distance_matrix):
                    solution = new_solution
                    improved = True
    return solution

def generate_initial_solution(cities, depot_city):
    solution = [depot_city] + random.sample(cities - {depot_city}, 4) + [depot_city]
    return solution

# Cities and their coordinates
coordinates = {
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

# Compute distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Setup
cities = set(coordinates.keys())
depot_city = 0

# GVNS parameters
num_restarts = 100
best_solution = None
best_cost = float('inf')

# GVNS Algorithm
for _ in range(num_restarts):
    current_solution = generate_initial_solution(cities, depot_city)
    current_cost = calculate_tour_cost(current_solution, distance_matrix)

    for _ in range(50):  # Number of iterations per restart
        shaken_solution = shake(current_solution[:], distance_matrix)
        improved_solution = variable_neighborhood_descent(shaken_solution, distance_matrix)
        improved_cost = calculate_tour_cost(improved_solution, distance_matrix)

        if improved_cost < current_cost:
            current_solution = improved_solution
            current_cost = improved_cost

    if current_cost < best_cost:
        best_solution = current_solution
        best_cost = current_cost

# Output best found solution
print("Tour:", best_solution)
print("Total travel cost:", best_cost)