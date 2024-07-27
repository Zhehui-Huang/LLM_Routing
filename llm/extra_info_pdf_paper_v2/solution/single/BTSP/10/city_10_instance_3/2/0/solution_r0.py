import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

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

# Simple heuristic to approximate the BTSP by finding a small-hamiltonian cycle
def find_btsp_tour(dist_matrix):
    num_cities = len(dist_matrix)
    # Starting at the depot city
    current_city = 0
    visited = set([current_city])
    tour = [current_city]
    max_distance = 0

    # Greedily pick next cities minimizing the maximum distance in the tour
    while len(visited) < num_cities:
        next_city = None
        min_edge_cost = float('inf')
        for j in range(num_cities):
            if j not in visited and dist_matrix[current_city][j] < min_edge_cost:
                next_city = j
                min_edge_cost = dist_matrix[current_city][j]
        visited.add(next_city)
        tour.append(next_city)
        max_distance = max(max_distance, min_edge_cost)
        current_city = next_city

    # Completing the cycle returning to the depot
    final_leg_distance = distance_matrix[current_city][0]
    max_distance = max(max_distance, final_leg_distance)
    tour.append(0)
    
    # Total cost of the cycle
    total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    return tour, total_cost, max_filtered_distance

tour, total_cost, max_distance = find_btsp_tour(distance_matrix)

# Display the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")