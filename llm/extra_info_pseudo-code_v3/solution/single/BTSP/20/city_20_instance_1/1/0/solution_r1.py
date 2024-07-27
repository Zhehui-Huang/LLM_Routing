import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def create_distance_matrix(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def find_bottleneck_tsp_tour(cities):
    n = len(cities)
    distance_matrix = create_distance_matrix(cities)
    
    # Generating all possible permutations of the city indices
    min_max_distance = float('inf')
    best_tour = None
    
    for perm in permutations(range(1, n)):
        # Creating the complete tour by adding the depot city around the permutation
        tour = [0] + list(perm) + [0]
        # Calculate the max distance in this tour
        max_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
    
    total_dist = sum(distance_matrix[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
    return best_tour, total_dist, min_max_distance

# Define the coordinates for each city
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculates the optimal tour using a Bottleneck TSP formulation
tour, total_cost, max_distance = find_bottleneck_tsp_tour(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)