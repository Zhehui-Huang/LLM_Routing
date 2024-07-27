import numpy as np
import random

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def generate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_line_distance(cities[i], cities[j])
    return distance_matrix

def generate_initial_solution(depot, cities):
    choose_cities = random.sample(cities, 3)
    solution = [depot] + choose_cities + [depot]
    return solution

def variable_neighborhood_descent(solution, distance_matrix):
    best_solution = solution[:]
    best_cost = calculate_total_distance(best_solution, distanceing_matrix)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                candidate_solution = best_solution[:]
                candidate_solution[i], candidate_solution[j] = candidate_solution[j], candidate_solution[i]
                candidate_cost = calculate_total_distance(candidate_solution, distance_matrix)
                if candidate_cost < best_cost:
                    best_solution = candidate_solution[:]
                    best_cost = candidate_cost
                    improved = True
    return best_solution

def shake(solution):
    idx = range(1, len(solution)-1)  # exclude first and last (depot)
    i1, i2 = random.sample(idx, 2)
    solution[i1], solution[i2] = solution[i2], solution[i1]
    return solution

def gvns_ktsp(cities, distance_matrix, nrst=100):
    depot = cities[0]
    other_cities = cities[1:]
    best_solution = generate_initial_solution(depot, other_cities)
    best_cost = calculate_total_distance(best_solution, distance_matrix)

    for _ in range(nrst):
        current_solution = generate_initial_solution(depot, other_cities)
        for _ in range(10):  # Shaking and local search loop
            shaken_solution = shake(current_solution[:])
            improved_solution = variable_neighborhood_descent(shaken_solution, distance_matrix)
            improved_cost = calculate_total_distance(improved_solution, distance_matrix)
            if improved_cost < best_cost:
                best_solution, best_cost = improved_solution, improved_cost

    return best_solution, best_cost

# Creating the cities list
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50),
    (21, 23), (88, 59), (79, 77), (63, 23),
    (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

distance_matrix = generate_distance_matrix(cities)
best_tour, best_cost = gvns_ktsp(cities, distance_matrix)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)