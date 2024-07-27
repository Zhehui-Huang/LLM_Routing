import random
import math

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two 2D points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour, distance_matrix):
    """ Calculate the total distance cost of the entire tour """
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return cost

def generate_initial_solution(all_cities, k=7):
    """ Generate an initial solution picking k cities at random, including the depot. """
    cities = [0] + random.sample(all_cities[1:], k-2) + [0]
    return cities

def shake(solution, distance_matrix):
    """ Shakes the solution by simple swaps. """
    candidate = solution[1:-1]  # keep the depot as is
    idx1, idx2 = random.sample(range(len(candidate)), 2)
    candidate[idx1], candidate[idx2] = candidate[idx2], candidate[idx1]
    return [0] + candidate + [0]

def vnd(tour, distance_matrix):
    """ Perform Variable Neighborhood Descent by simple two-swap descent method. """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-1):
            for j in range(i+1, len(tour)-1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                if total_tour_cost(new_tour, distance_matrix) < total_tour_cost(tour, distance_matrix):
                    tour = new_tour
                    improved = True
    return tour

def gvns(cities, distance_matrix, n_restarts=100):
    best_solution = None
    best_cost = float('inf')
    for _ in range(n_restarts):
        current_solution = generate_initial_solution(cities)
        current_solution = vnd(current_solution, distance_matrix)
        current_cost = total_tour_cost(current_solution, distance_matrix)
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

        for _ in range(20):  # Intense local search
            shaken_solution = shake(current_solution, distance_matrix)
            improved_solution = vnd(shaken_solution, distance_matrix)
            improved_cost = total_tour_cost(improved_solution, distance_matrix)
            if improved_cost < best_cost:
                best_solution = improved_dataanalysis_solution
                best_cost = improved_cost

    return best_solution, best_cost

# Define the city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Pre-compute distances
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Solve using GVNS
best_tour, min_cost = gvns(cities, distance_matrix)
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))