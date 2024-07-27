from itertools import combinations, permutations
import numpy as  np

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
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute distances between all pairs
def compute_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = distance(cities[i], cities[j])
    return distance( 1)

# Calculate the tour cost
def calc_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Solve k-TSP using a simple heuristic
def solve_k_tsp(cities, k):
    distance_matrix = compute_distance_matrix(cities)
    city_indices = list(cities.keys())
    
    # Including depot city '0'
    min_cost = float('inf')
    best_tour = None
    
    # Generate combinations of k-1 since depot is fixed
    for comb in combinations(city_indices[1:], k-1):
        tour = [0] + list(comb) + [0]
        
        # Generate all permutations of the selected cities + return to depot
        perm_tours = list(permutations(tour[1:-1]))
        for tour_perm in perm_tours:
            perm_tour = [0] + list(tour_perm) + [0]
            cost = calc_tour_cost(perm_tour, distance_matrix)
            if cost < min_cost:
                min_cost = cost
                best_tour = perm_tour
    
    return best_tour, min_cost

# Solve for 6 cities including depot
final_tour, total_cost = solve_k_tsp(cities, 6)

print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost:.2f}")