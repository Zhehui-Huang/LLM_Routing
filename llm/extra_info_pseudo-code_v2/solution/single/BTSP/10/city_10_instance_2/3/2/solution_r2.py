import math
import itertools

# Calculate the Euclidean distance between any two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate a distance matrix for all city pairs
def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

# Evaluate the tour to calculate total distance and max distance between any two cities
def evaluate_tour(tour, distance_matrix):
    total_distance = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_distance, max_distance

# Implements the TSP to minimize the maximum distance between consecutive cities
def solve_tsp(cities):
    num_cities = len(cities)
    distance_matrix = create_distance_matrix(cities)
    all_permutations = itertools.permutations(range(1, num_cities))
    best_tour = None
    best_max_distance = float('inf')
    best_total_distance = float('inf')
    
    for permutation in all_permutations:
        current_tour = [0] + list(permutation) + [0]
        total_distance, max_distance = evaluate_tour(current_tour, distance_matrix)
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_distance < best_total_distance):
            best_max_distance = max_distance
            best_total_distance = total_distance
            best_tour = current_tour
            
    return best_tour, best_total_distance, best_max_distance

# Define cities and their coordinates
cities = [
    (90, 3),  # City 0 - Depot
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Solve the TSP problem
tour, total_cost, max_distance = solve_tst(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)