import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities coordinates {index: (x, y)}
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate all possible pairwise distances
edges = {}
for i in cities:
    for j in cities:
        if i != j:
            edges[(i, j)] = euclidean_distance(cities[i], cities[j])

# Function to check if a permutation forms a valid path with edges below a certain weight
def valid_tour(permutation, max_edge_weight):
    for i in range(len(permutation)-1):
        if edges[(permutation[i], permutation[i+1])] > max_edge_weight:
            return False
    return True

def find_bottleneck_tsp():
    # Consider permutations starting from the depot only
    city_indices = list(cities.keys())[1:]  # Exclude depot (0)
    all_perms = permutations(city_indices)
    
    min_max_distance = float('inf')
    best_tour = None
    
    # Check each permutation for feasibility under increasing weights
    for perm in all_perms:
        tour = [0] + list(perm) + [0]  # Adding depot at start and end
        max_edge_weight_in_tour = max(edges[(tour[i], tour[i+1])] for i in range(len(tour)-1))
        
        # Check if this permutation is better
        if max_edge_weight_in_tour < min_max_distance:
            min_max_difference = max_edge_weight_in_tour
            best_tour = tour
            
    # Calculate total travel cost and max distance in the best tour found
    if best_tour:
        total_distance = sum(edges[(best_tour[i], best_tour[i+1])] for i in range(len(best_tour)-1))
        max_distance = max(edges[(best_tour[i], best_tour[i+1])] for i in range(len(best_tour)-1))
        
        return best_tour, total_distance, max_distance
    
    return [], 0, 0

# Find the optimal tour solution and print the results
tour, total_cost, max_distance = find_bottleneck_tsp()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")