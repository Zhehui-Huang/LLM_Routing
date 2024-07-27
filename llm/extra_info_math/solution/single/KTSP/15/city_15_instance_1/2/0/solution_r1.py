import numpy as np
from itertools import combinations, permutations

# Define city coordinates
city_coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

# Calculate route distance
def evaluate_route(route, dist_matrix):
    total_distance = 0
    num_stops = len(route)
    for i in range(1, num_stops):
        total_distance += dist_matrix[route[i - 1]][route[i]]
    total_distance += dist_matrix[route[-1]][route[0]]  # Return to depot
    return total_distance

# Distance Matrix
dist_matrix = calculate_distance_matrix(city_coords)

# Generate all routes selecting 6 cities (including depot)
def find_shortest_tour():
    num_cities = len(city_coords)
    best_route = None
    best_distance = float('inf')
    
    # Iterate over combinations of 5 cities excluding the depot
    for combination in combinations(range(1, num_cities), 5):
        current_combination = [0] + list(combination)  # Include depot
        # Permute all possible orders of visiting these cities
        for perm in permutations(current_combination[1:]):
            route = [0] + list(perm) + [0]  # start and end at depot
            distance = evaluate_route(route, dist_matrix)
            if distance < best_distance:
                best_distance = distance
                best_route = route
    
    return best_route, best_distance

# Execute the function and print result
shortest_tour, shortest_distance = find_shortest_tour()
print("Tour:", shortest_tour)
print("Total travel cost:", shortest_distance)