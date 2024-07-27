import math
from itertools import permutations

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 
    4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70), 
    8: (20, 99), 9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Precompute distances between all pairs of cities
distance_matrix = {}
for c1 in cities:
    for c2 in cities:
        distance_matrix[(c1, c2)] = euclidean_distance(c1, c2)

# Heuristic function to find approximate solution for k-TSP
def k_tsp_gvns(cities, k):
    # Start with initial subset starting with the depot
    initial_subset = [0] + list(range(1, k))  # E.g., [0, 1, 2, ..., k-1]
    best_tour = None
    best_cost = float('inf')
    
    permutations_pool = permutations(initial_subset[1:])
    for perm in permutations_pool:
        current_tour = [0] + list(perm) + [0]
        current_cost = sum(distance_matrix[(current_tour[i], current_tour[i+1])] for i in range(len(current_tour)-1))
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
            
    return best_tour, best_cost

# Solve k-TSP for k=8 (including the depot city)
k = 8
result_tour, result_cost = k_tsp_gvns(list(cities.keys()), k)

# Output format
print("Tour:", result_tour)
print("Total travel cost:", round(result_cost, 2))