import numpy as np
import random
import itertools

# City coordinates
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
    8: (49, 29), 9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate distance matrix
def create_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in cities:
        for j in cities:
            if i != j:
                distance_matrix[i][j] = calc_distance(i, j)
    return distance_matrix

distance_matrix = create_distance_matrix(cities)

# Generate initial solution
def generate_initial_solution(cities, k=6):
    return [0] + random.sample(list(cities.keys())[1:], k-2) + [0]

# Calculate total travel cost
def solution_cost(solution, distance_matrix):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += distance_matrix[solution[i]][solution[i + 1]]
    return total_cost

# Shake function: changes the set of cities in the tour
def shake(solution, k):
    base_solution = solution[1:-1]
    possible_cities = set(cities.keys()) - set(base_solution)
    city_to_remove = random.choice(base_solution)
    city_to_add = random.choice(tuple(possible_cities))
    new_solution = [0] + [city_to_add if x == city_to_remove else x for x in base_solution] + [0]
    return new_solution

# Variable Neighborhood Descent
def vnd(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if j != i:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = solution_cost(new_solution, distance_matrix)
                    current_cost = solution_cost(solution, distance_matrix)
                    if new_cost < current_cost:
                        solution = new_solution
                        improved = True
                        break
            if improved:
                break
    return solution

# General Variable Neighborhood Search
def gvns(cities, k, nrst, distance_matrix):
    best_solution = generate_initial_solution(cities, k)
    best_cost = solution_cost(best_solution, distance_matrix)
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, k)
        current_cost = solution_cost(current_solution, distance_matrix)
        while True:
            new_solution = vnd(shake(current_solution, k), distance_matrix)
            new_cost = solution_cost(new_solution, distance_matrix)
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
            else:
                break
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    return best_solution, best_cost

# Run GVNS with specific parameters
best_solution, best_cost = gvns(cities, 6, 100, distance_matrix)

# Output format:
print("Tour:", best_solution)
print("Total travel cost:", best_cost)