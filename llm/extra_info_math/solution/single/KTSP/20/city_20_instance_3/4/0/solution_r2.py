import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean

def create_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Create distance matrix
distance_matrix = create_distance_matrix([cities[i] for i in cities])

# Find subset of cities including the depot
city_indices = list(cities.keys())
k = 13

def find_shortest_path(distance_matrix, city_indices, k):
    best_tour = None
    best_cost = float('inf')
    
    for subset in permutations(city_indices[1:], k - 1):  # Generate permutations of k-1 cities excluding the depot
        tour = [0] + list(subset) + [0]
        cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
            
    return best_tour, best_cost

best_tour, best_cost = find_shortest_path(distance_distance_matrix, hierarchy_indices, k)

# Output the results:
print("Tour:", best_tour)
print("Total travel cost:", best_cost)