import numpy as np
import random
from itertools import permutations

# Define the coordinates of the cities including the depot
coords = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Helper function: Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return np.hypot(c1[0] - c2[0], c1[1] - c2[1])

# Generate the distance matrix between all cities
def generate_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean_wistance(coords[i], coords[j])
    return distance_matrix

# Generate a random initial solution (Visiting exactly 6 cities including depot)
def generate_initial_solution(V):
    solution = [0]
    solution += random.sample(list(V.keys())[1:], 5)  # Choose 5 additional cities
    solution.append(0)  # Return to the depot
    return solution

# Evaluate the total travel cost of the tour using the distance matrix
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Two-opt swap used in local search
def two_opt_swap(tour):
    n = len(tour)
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour, distance_matrix)
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 1):
            for j in range(i + 2, n - 1): 
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = calculate_tour_cost(new_tour, distance_matrix)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
                    improved = True
    return best_tour, best_cost

# General Variable Neighborhood Search (GVNS) Algorithm
def GVNS(k, coords, num_restarts):
    V = coords
    best_tour = []
    best_cost = float('inf')
    distance_matrix = generate_distance_matrix(V)

    for _ in range(num_restarts):
        initial_tour = generate_initial_solution(V)
        tour, cost = two_opt_swap(initial_tour)

        if cost < best_cost:
            best_tour, best_cost = tour, cost

    return best_tour, best_cost

# Run the algorithm
num_cities_to_visit = 6
num_restarts = 50
best_tour, best_cost = GVNS(num_cities_to_visit, coords, num_restarts)

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost: {:.2f}".format(best_cost))