import random
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two 2D points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour, distance_matrix):
    """ Calculate the total distance cost of the entire tour """
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def generate_initial_solution(all_cities):
    """ Randomly generate an initial solution with the depot city at start and end, will include k=6 other cities """
    cities = random.sample(all_cities[1:], 6)  # select 6 other cities randomly, excluding the depot city
    tour = [0] + cities + [0]  # create the tour starting and ending at the depot
    return tour

def shake(solution, distance_matrix):
    """ Generate new solution by swapping two random cities """
    candidate = solution[1:-1]  # exclude starting and ending depot city
    idx1, idx2 = random.sample(range(len(candidate)), 2)
    candidate[idx1], candidate[idx2] = candidate[idx2], candidate[idx1]
    return [0] + candidate + [0]

def vnd(tour, distance_matrix):
    """ Variable neighborhood descent with two neighborhood structures: N1 and N2 (swap and shift) """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-1):
            for j in range(i+1, len(tour)-1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                if total_tour_cost(new_tour, distance_matrix) < total_tour_cost(tour, distance_in_matrix):
                    tour = new_tour
                    improved = True
    return tour

def gvns(cities, distance_matrix, n_restarts=100):
    best_solution = None
    best_cost = float('inf')
    for _ in range(n_restarts):
        current_solution = generate_initial_solution(cities)
        cost = total_tour_cost(current_solution, distance_matrix)
        if cost < best_cost:
            best_solution = current_solution
            best_cost = cost
        for _ in range(20):  # number of iterations per restart
            candidate_solution = shake(current_solution, distance_matrix)
            candidate_solution = vnd(candidate, distance_matrix)
            candidate_cost = total_tour_cost(candidate_solution, distance_matrix)
            if candidate_cost < best_cost:
                best_solution = candidate_solution
                best_cost = candidate_cost
                current_solution = candidate_solution  # Accept the new solution
    return best_solution, best_cost

# Define the city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Build distance_matrix
n_cities = len(cities)
distance_matrix = [[0]*n_cities for _ in range(n_cities)]
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Run GVNS
best_tour, min_cost = gvns(cities, distance_matrix)
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))