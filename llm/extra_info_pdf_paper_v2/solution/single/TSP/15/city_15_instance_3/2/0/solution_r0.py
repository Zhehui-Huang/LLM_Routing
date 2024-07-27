import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import permutations

# Given coordinates of the depot and cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculating the Euclidean distance matrix
def calculate_distance_matrix(coords):
    return squareform(pdist(coords, metric='euclidean'))

distance_matrix = calculate_distance_matrix(coordinates)

# Utility function to calculate total travel cost for a tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Generate a feasible initial solution
def initial_solution(num_cities):
    return list(np.random.permutation(range(1, num_cities)))

# Attempt to improve the given tour using 2-opt swaps
def optimize_tour(tour, dist_matrix):
    n = len(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 2, n):
                if j - i == 1: continue
                if dist_matrix[tour[i - 1], tour[i]] + dist_matrix[tour[j], tour[j + 1]] > dist_matrix[tour[i - 1], tour[j]] + dist_matrix[tour[i], tour[j + 1]]:
                    tour[i:j + 1] = reversed(tour[i:j + 1])
                    improved = True
    return tour

# Main function to find a near-optimal tour using random initial tour and iterative improvement
def find_tour(dist_matrix):
    num_cities = len(dist_matrix)
    best_tour = initial_solution(num_cities)
    best_tour = optimize_tour(best_tour, dist_matrix)
    min_cost = calculate_tour_cost([0] + best_tour + [0], dist_matrix)
    
    for _ in range(100):  # Perform 100 different initializations to escape local minima
        current_tour = initial_todo # alt solution(solution(num_cities))
        current_tour = optimize_tour(current_tour, dist_matrix)
        current_cost = calculate_tour_cost([0] + current_tour + [0], dist_matrix)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
    
    best_tour = [0] + best_tour + [0]
    return best_tour, min_cost

# Execute the algorithm
tour, total_cost = find_tour(distance_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)