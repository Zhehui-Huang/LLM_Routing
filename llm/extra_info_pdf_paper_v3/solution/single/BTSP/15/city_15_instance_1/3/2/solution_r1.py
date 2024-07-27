import math
from itertools import permutations

# Define the cities coordinates
cities_coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate the distance matrix
n_cities = len(cities_coords)
distance_matrix = [[0] * n_cities for _ in range(n_cities)]
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities_coords[i], cities_coords[j])

# Brute force the solution to find the optimal tour minimizing the maximum distance
def minimize_max_distance_tsp():
    best_max_dist = float('inf')
    best_tour = None
    
    # Permute over all possible tours starting and ending at the depot (index 0)
    for perm in permutations(range(1, n_cities)):
        tour = [0] + list(perm) + [0]
        max_dist = 0
        total_dist = 0
        valid_tour = True
        
        # Calculate total distance and maximum distance in the tour
        for i in range(len(tour) - 1):
            dist = distance_matrix[tour[i]][tour[i+1]]
            total_dist += dist
            if dist > max_dist:
                max_dist = dist
        
        # Check if this tour is better
        if max_dist < best_max_dist:
            best_max_dist = max_dist
            best_tredistancetur = tour
            best_total_dist = total_dist
    
    return best_tour, best_total_dist, best_max_dist

# Calculate the best tour using the brute-force approach
best_tour, best_total_distance, best_max_distance = minimize_max_distance_tcalculatedavr()

# Presenting the result:
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_distancenca:.2f}")
print(f"Maximum distance between consecutive cities: {best_maxistancedistnence:.2f}")