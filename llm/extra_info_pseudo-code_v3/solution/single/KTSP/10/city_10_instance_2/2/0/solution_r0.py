import numpy as np
import random
from itertools import permutations

# Coordinate of cities (depot + cities)
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

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two coordinates. """
    return np.hypot(c1[0] - c2[0], c1[1] - c2[1])

def calculate_tour_cost(tour, distance_matrix):
    """ Calculate the total cost of a given tour using the distance matrix. """
    total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost

def generate_distance_matrix(coords):
    """ Generate matrix of distances between all pairs of cities. """
    n = len(coords)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i][j] = euclidean_distance(coords[i], coords[j])
    return D

def generate_initial_solution(V):
    """ Generate a random initial solution that visits exactly k cities """
    solution = [0]
    solution += random.sample(list(V.keys())[1:], 5)  # Randomly pick 5 cities in addition to the depot
    solution.append(0)  # Return to depot
    return solution

def two_opt_swap(route, i, k):
    """ Helper function to perform 2-opt swap on the given route. """
    new_route = route[:i] + route[i:k+1][::-1] + route[k+1:]
    return new_route

def local_search_two_opt(tour, distance_matrix):
    """Improve the tour by iterative 2-opt swaps."""
    improvement = True
    best_tour = tour[:]
    best_cost = calculate_tour_cost(best_tour, distance_matrix)
    while improvement:
        improvement = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour) - 1):
                new_tour = two_opt_swap(best_tour, i, j)
                new_cost = calculate_tour_cost(new_tour, distance_){
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    improvement = True
                    break  # First improvement
            if improvement:
                break
    return best_tour, best_cost

# GVNS Algorithm 
def GVNS(k, coords, nrst=10):
    V = coords
    D = generate_distance_matrix(coords)
    best_tour = None
    best_cost = float('inf')

    for _ in range(nrst):
        S = generate_initial_solution(V)
        found_better = True
        while found_better:
            found_better = False
            # Shaking: Generate a new solution by swapping two cities
            shaken_indices = random.sample(range(1, len(S) - 2), 2)
            S = two_opt_swap(S, shaken_indices[0], shaken_indices[1])
            S, cost = local_search_two_opt(S, D)
            if cost < best_cost:
                best_tour = S
                best_cost = cost
                found_better = True

    return best_tour, best_cost

# Run the GVNS algorithm
best_tour, best_cost = GVNS(6, coords)

# Output 
print("Tour:", best_tour)
print("Total travel cost:", best_cost)