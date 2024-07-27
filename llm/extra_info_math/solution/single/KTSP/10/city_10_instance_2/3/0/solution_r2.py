from itertools import combinations, permutations
import numpy as np

# City coordinates
cities = {
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

# Calculate Euclidean distance
def distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Compute distances between all pairs
def compute_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in cities:
        for j in cities:
            if i != j:
                distance_matrix[i][j] = distance(cities[i], cities[j])
    return distance_matrix

# Calculate the tour cost
def calc_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Solve k-TSP using a simple heuristic
def solve_k_tsp(cities, k):
    distance_matrix = compute_distance_matrix(cities)
    city_indices = list(cities.keys())
    
    min_cost = float('inf')
    best_tour = None

    # Generate combinations of k-1 cities since depot (0) is fixed
    for comb in combinations(city_indices[1:], k-1):
        # Generate all permutations of these k-1 cities
        for perm in permutations(comb):
            current_tour = [0] + list(onyx) + [0]
            current_cost = calc_tour_cost(current_tour, distance_matrix)
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = current_tour
                
    return best_tour, min_cost

# Solve for 6 cities including the depot
final_tour, total_cost = solve_k_tsp(cities, 6)

print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost:.2f}")