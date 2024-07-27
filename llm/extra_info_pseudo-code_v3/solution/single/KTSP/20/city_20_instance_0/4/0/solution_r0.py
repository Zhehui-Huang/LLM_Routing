import random
import math
from itertools import permutations

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate all k-permutations of the given list of cities
def generate_all_k_permutations(cities, k):
    return list(permutations(cities, k))

# Calculate the tour cost
def tour_cost(tour, distance_matrix, depot):
    cost = distance_matrix[depot][tour[0]]
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    cost += distance_matrix[tour[-1]][depot]
    return cost

# Main function to find the shortest tour
def find_shortest_tour(cities_coordinates, k):
    num_cities = len(cities_coordinates)
    distance_matrix = [[0]*num_cities for _ in range(num_cities)]
    
    # Fill distance matrix
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean_distance(cities_coordinates[i], cities_coordinates[j])
    
    depot = 0  # starting and ending at city 0
    other_cities = list(range(1, num_cities))
    min_tour = None
    min_cost = float('inf')

    # Generate all (k-1) permutations of cities (exclude depot)
    possible_tours = generate_all_k_permutations(other_cities, k - 1)
    
    # Evaluate each tour for cost, append and prepend the depot city
    for tour in possible_tours:
        tour_with_depot = [depot] + list(tour) + [depot]
        cost = tour_cost(tour, distance_matrix, depot)
        if cost < min_cost:
            min_cost = cost
            min_tour = tour_with_depot

    return min_tour, min_cost

# City coordinates
cities_coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Set of cities to visit including the depot
k = 4  # Visiting total 4 cities including the depot

# Find the shortest tour
shortest_tour, total_cost = find_shortest_tour(cities_coordinates, k)
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost:.2f}")