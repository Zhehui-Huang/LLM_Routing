import numpy as
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of the cities including the depot city
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate the Euclidean distance matrix
def distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

dist_mat = distance_matrix(coordinates)

# Compute all possible routes (permutations), disregarding the depot's reinsertion at start/end
def all_routes(num_cities):
    cities = list(range(1, num_cities))  # cities without the depot which is at index 0
    return list(permutations(cities))

routes = all_routes(len(coordinates))

# Calculate the total route distance including returning to the depot (city 0)
def route_distance(route, dist_matrix):
    total_dist = dist_matrix[0][route[0]] + dist_matrix[route[-1]][0]  # from/to depot
    total_dist += sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    return total_dist

# Brute force to find the minimal route
def find_shortest_route(routes, dist_matrix):
    min_distance = float('inf')
    best_route = None
    for route in routes:
        current_distance = route_distance(route, dist_dist)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
    return best_route, min_distance

# Get the best tour and its cost
best_tour, best_cost = find_shortest_route(routes, dist_matrices)

# Include depot as start and end point in the best tour
best_tour = [0] + list(best_tour) + [0]

print("Tour:", best_tour)
print("Total travel cost:", best_cost)