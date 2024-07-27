import numpy as np
import itertools

# City coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Function to calculate Euclidean distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    mat = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            mat[i][j] = np.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1])
    return mat

# Calculates total travel cost of a tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Distance matrix
dist_matrix = calculate_distance_matrix(cities)

# Finding shortest k-TSP tour using a heuristic
def find_shortest_k_tsp_tour(dist_matrix, k):
    num_cities = len(cities)
    all_indices = set(range(num_cities))
    subsets = list(itertools.combinations(all_indices - {0}, k-1))

    best_tour = None
    best_cost = float('inf')
    for subset in subsets:
        for perm in itertools.permutations(subset):
            tour = [0] + list(perm) + [0]
            cost = calculate_tour_cost(tour, dist_matrix)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
    return best_tour, best_cost

best_tour, best_cost = find_shortest_k_tsp_tour(dist_matrix, 10)  # k = 10 including the depot

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)