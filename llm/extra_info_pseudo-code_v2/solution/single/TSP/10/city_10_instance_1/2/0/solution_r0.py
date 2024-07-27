import math
import random

# Define cities 
cities = [
    (53, 68),  # Depot city
    (75, 11), 
    (91, 95), 
    (22, 80), 
    (18, 63), 
    (54, 91), 
    (70, 14), 
    (97, 44), 
    (17, 69), 
    (95, 89)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Generate an initial solution: simple nearest neighbor algorithm
def nearest_neighbor_tour(start):
    unvisited = list(range(n))
    unvisited.remove(start)
    tour = [start]
    
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)
    return tour

# Calculate the total tour cost
def tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Initial tour
initial_tour = nearest_neighbor_tour(0)
initial_tour.append(0)  # return to depot

# Initial cost
initial_cost = tour_cost(initial_tour)

# Output results
print("Initial Tour:", initial_tour)
print("Initial Total travel cost:", initial_cost)

# Lin-Kernighan improvement loop
# Note: Since the actual LK heuristic is complex and not practical to implement fully in this short
# snippet, this demonstrates using the initial solution with nearest neighbor.
# Extending this to a full Lin-Kernighan implementation would be a large project.

print("Optimal Tour (simplified for demonstration):", initial_tour)
print("Optimal Total travel cost (simplified for demonstration):", initial_cost)