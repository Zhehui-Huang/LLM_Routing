import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates
cities = [
    (84, 67), # City 0: Depot
    (74, 40), # City 1
    (71, 13), # City 2
    (74, 82), # City 3
    (97, 28), # City 4
    (0, 31),  # City 5
    (8, 62),  # City 6
    (74, 56), # City 7
    (85, 71), # City 8
    (6, 76)   # City 9
]

# Calculate Euclidean distances between all pairs of cities
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

distance_matrix = calculate_distances(cities)

# Simple heuristic to approximate the BTSP by finding a tour minimizing the maximum leg distance
def find_btsp_tour(dist_matrix):
    num_cities = len(dist_matrix)
    all_tours = permutations(range(1, num_cities))
    min_max_leg_distance = float('inf')
    best_tour = None

    for tour in all_tours:
        full_tour = [0] + list(tour) + [0]
        max_leg_distance = max(dist_matrix[full_tour[i]][full_tour[i+1]] for i in range(len(full_tour)-1))
        
        if max_leg_distance < min_max_leg_distance:
            min_max_leg_distance = max_leg_distance
            best_tour = full_tour

    total_cost = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    
    return best_tour, total_cost, min_max_leg_distance

tour, total_cost, max_distance = find_btsp_tour(distance_matrix)

# Display the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")