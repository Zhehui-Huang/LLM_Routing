import numpy as np
import random

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.hypot(city1[0] - city2[0], city1[1] - city2[1])

# Function to compute fitness of a solution
def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Generate the distance matrix for the given cities
def generate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = distance_matrix[j][i] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

# Generate initial solution (randomly)
def generate_initial_solution(depot, cities):
    solution = [depot] + random.sample(cities, 3) + [depot]
    return solution

# Local improvement using two different neighborhood structures
def variable_neighborhood_descent(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        # N2 neighborhood: Swap positions
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solu...
                    new_cost = calculate_total_distance(new_solution, distance_matrix)
                    if new_cost < calculate_total_distance(solution, distance_matrix):
                        solution = new_solution
                        improved = True
    return solution

# Shaking the solution by swapping two randomly selected cities
def shake(solution, k):
    city_idx = random.sample(range(1, len(solution)-1), 2)
    new_solution = solution[:]
    new_solution[city_idx[0]], new_solution[city_idx[1]] = new_solution[city_idx[1]], new_solution[city_idx[0]]
    return new_solution

# GVNS algorithm
def gvns_ktsp(cities, distance_matrix, nrst=10):
    depot = cities[0]
    other_cities = cities[1:]
    best_solution = generate_initial_solution(depot, other_cities)
    best_cost = calculate_total_distance(best_solution, distance_matrix)

    for _ in range(nrst):
        current_solution = generate_initial_solution(depot, other_cities)
        current_cost = calculate_total_distance(current_solution, distance_matrix)
        
        k = 1
        while k < 3:
            new_solution = shake(current_solution, k)
            new_solution = variable_neighborhood_descent(new_solution, distanc...
            new_cost = calculate_total_distance(new_solution, distance_matrix)
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
                k = 1  # Reset neighborhood indicator
            else:
                k += 1

        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
        
    return best_solution, best_cost

# Cities are defined as tuples with their coordinates
cities = [
    (9, 93),  # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39),
]

distance_matrix = generate_distance_matrix(cities)
best_tour, best_cost = gvns_ktsp(cities, distance_matrix)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))