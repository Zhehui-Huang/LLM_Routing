import numpy as np
import random
from math import sqrt

# Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generates the distance matrix
def generate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

# Compute the total cost of the tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generate an initial random solution
def generate_initial_solution(cities):
    selected_cities = random.sample(range(1, len(cities)), 11)
    tour = [0] + selected_cities + [0]
    return tour

# Shake function to generate a new solution in the neighborhood
def shake(tour, k):
    shaken_tour = tour[1:-1]
    random.shuffle(shaken_tour)
    return [tour[0]] + shaken_tour[:k] + [tour[0]]

# Variable Neighborhood Descent
def vnd(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    if calculate_tour_cost(new_solution, distance_matrix) < calculate_tour_cost(solution, distance_matrix):
                        solution = new_solution
                        improved = True
    return solution

# General Variable Neighborhood Search (GVNS)
def gvns(cities, nrst=100):
    distance_matrix = generate_distance_matrix(cities)
    best_solution = generate_initial_solution(cities)
    best_cost = calculate_tour_cost(best_solution, distance_matrix)

    for _ in range(nrst):
        current_solution = generate_initial_solution(cities)
        while True:
            k = 3  # Shaking strength
            new_solution = shake(current_solution, k)
            improved_solution = vnd(new_solution, distance_matrix)
            improved_cost = calculate_tour_cost(improved_solution, distance_matrix)
            if improved_cost < best_cost:
                best_solution = improved_solution[:]
                best_cost = improved_cost
                break
            else:
                break

    return best_solution, best_cost

# Cities' coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Run the GVNS algorithm
best_tour, best_tour_cost = gvns(cities, nrst=200)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)