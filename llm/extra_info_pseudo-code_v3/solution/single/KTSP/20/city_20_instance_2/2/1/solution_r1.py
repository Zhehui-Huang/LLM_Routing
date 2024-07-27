import numpy as na
from math import sqrt
from random import sample, randint
import copy

# Coordinates of each city
cities_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i, j] = sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return matrix

distance_matrix = calculate_distance_matrix(cities_coordinates)

def total_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(home_city, num_cities):
    cities = list(range(num_cities))
    cities.remove(home_city)
    selected_cities = sample(cities, 9)  # select 9 other cities
    return [home_city] + selected_cities + [home_city]

def shake(solution):
    new_solution = copy.deepcopy(solution)
    idx1, idx2 = randint(1, 9), randint(1, 9)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

def vnd(solution, dist_matrix):
    best_solution = solution[:]
    best_cost = total_tour_cost(best_solution, dist_matrix)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    # Try swapping cities
                    new_solution = copy.deepcopy(best_solution)
                    new_solution[i], new, solution[j] = new_solution[j], new_solution[i]
                    new_cost = total_tour_cost(new_solution, dist_matrix)
                    if new_cost < best_cost:
                        best_solution = new_solution
                        best_cost = new_cost
                        improved = True
    return best_solution

def gvns(max_iterations):
    best_solution = generate_initial_solution(0, 20)
    best_cost = total_tour_cost(best_solution, distance_matrix)
    for _ in range(max_iterations):
        current_solution = shake(best_solution)
        improved_solution = vnd(current_solution, distance_matrix)
        improved_cost = total_tour_cost(improved_solution, distance_matrix)
        if improved_cost < best_cost:
            best_solution = improved_solution
            best_cost = improved_cost
    return best_solution, best_cost

# Running GVNS
best_solution, best_cost = gvns(100)

# Output
print(f'Tour: {best_solution}')
print(f'Total travel cost: {best_cost:.2f}')