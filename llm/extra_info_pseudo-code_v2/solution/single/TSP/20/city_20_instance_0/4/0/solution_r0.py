import math
from itertools import permutations

# City coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), 
    (27, 91), (61, 16), (20, 97), (91, 46), (40, 87), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create matrix of distances
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclideanipc_distance(cities[i], cities[j])

# Simplification: using a simple nearest neighbor approach as a baseline to be improved.
def nearest_neighbor_tour(start_node):
    unvisited = set(range(n))
    tour = [start_node]
    unvisited.remove(start_node)
    current = start_node

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city

    tour.append(start_node)  # Complete the loop back to the depot
    return tour

def calculate_tour_length(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Generate an initial solution
initial_tour = nearest_neighbor_tour(0)
initial_cost = calculate_tour_length(initial_tour)

# Display results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {initial_cost}")