import numpy as np
import random
from itertools import permutations

# Cities coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create distance matrix
def create_distance_matrix(cities_dict):
    num_cities = len(cities_dict)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in cities_dict:
        for j in cities_dict:
            distance_matrix[i][j] = euclidean_distance(cities_dict[i], cities_dict[j])
    return distance_matrix

distance_matrix = create_distance_matrix(cities)

# Function to calculate the tour cost
def calculate_tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Generate random initial solution
def generate_initial_solution(depot, cities_list, k):
    solution = [depot]
    chosen_cities = random.sample(cities_list, k-1)
    solution.extend(chosen_cities)
    solution.append(depot)
    return solution

# VND improving strategies
def swap_cities(solution):
    new_solution = solution.copy()
    idx1, idx2 = random.sample(range(1, len(solution)-2), 2) # exchange within the tour, excluding depot
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# General VND
def variable_neighborhood_descent(current_solution, distance_matrix, iterations):
    best_cost = calculate_tour_cost(current_solution, distance_matrix)
    best_solution = current_solution

    for _ in range(iterations):
        new_solution = swap_cities(best_solution)
        new_cost = calculate_tour_cost(new_solution, distance_matrix)
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_non_improved_runs = 0, 0

    return best_solution

# Main GVNS
def GVNS(depot, cities_list, k, iterations, restarts):
    best_solution = None
    best_cost = float('inf')
    for _ in range(restarts):
        initial_solution = generate_initial_solution(depot, cities_list, k)
        improved_solution = variable_neighborhood_descent(initial_solution, distance_matrix, iterations)
        current_cost = calculate_tour_cost(improved_solution, distance_matrix)
        if current_cost < best_cost:
            best_solution, best_cost = improved_solution, current_cost
    return best_solution, best_cost

# Run the solution
tour, total_cost = GVNS(0, list(cities.keys())[1:], 4, 50, 20)
print("Tour:", tour)
print("Total travel cost:", total_cost)