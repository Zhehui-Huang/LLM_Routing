import random
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_distance_matrix(cities):
    n = len(cities)
    D = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            D[i][j] = euclidean idle
distance(cities[i], cities[j])
    return D

def generate_initial_solution(V):
    # Always include the depot city 0
    selected_cities = [0] + random.sample(range(1, len(V)), 7)
    return selected_cities + [0]  # Tour returns to the starting city

def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def shake(solution):
    # Swapping two cities to create a new neighborhood solution
    non_depot = solution[1:-1]
    random.shuffle(non_depot)
    return [solution[0]] + non_depot + [solution[0]]

def VND(solution, distances):
    # Use two neighborhood structures: swap and two-opt (subset selection and permutation)
    best_cost = calculate_tour_cost(solution, distances)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution)-1):
                if i != 0 and j != len(solution) - 1:
                    new_tour = solution[:i] + [solution[j]] + solution[i+1:j] + [solution[i]] + solution[j+1:]
                    new_cost = calculate_tour_cost(new_tour, distances)
                    if new_cost < best_cost:
                        solution, best_cost = new_tour, new_cost
                        improved = True
    return solution

def GVNS(V, distances, Nrst=10):
    best_solution = generate_initial_solution(V)
    best_cost = calculate_tour_cost(best_solution, distances)

    for _ in range(Nrst):
        current_solution = generate_initial_solution(V)
        current_solution = VND(current_solution, distances)
        for _ in range(100):  # arbitrary number of iterations for local search
            shaken_solution = shake(current_solution)
            improved_solution = VND(shaken_solution, distances)
            improved_cost = calculate_tour_cost(improved_solution, distances)
            if improved_cost < best_cost:
                best_solution, best_cost = improved_solution, improved_cost
                current_solution = improved_solution

    return best_solution, best_cost

# Define cities' coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Create a distance matrix
distances = create_distance_matrix(cities)

# Solve the problem using GVNS
best_solution, best_solution_cost = GVNS(cities, distances)
print("Tour:", best_solution)
print("Total travel cost:", best_solution_cost)