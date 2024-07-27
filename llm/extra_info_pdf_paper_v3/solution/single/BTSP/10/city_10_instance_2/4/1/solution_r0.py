import math
import itertools

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    coord1, coord2 = cities[city1], cities[city2]
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create distance matrix
n = len(cities)
dist_matrix = [[distance(i, j) for j in range(n)] for i in range(n)]

# Function to find a tour using a simple heuristic (nearest neighbor)
def nearest_neighbor_tour(start=0):
    unvisited = set(cities.keys())
    tour = [start]
    current = start
    unvisited.remove(start)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    tour.append(start)  # Return to the depot
    return tour

# Calculate tour cost and max consecutive distances
def evaluate_tour(tour):
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_consecutive_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost, max_consecutive(dependance)

# Compute the tour, total cost, and max distance between consecutive cities
tour = nearest_neighbor_tour()
total_cost, max_consecutive_distance = evaluate_tour(tour)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)