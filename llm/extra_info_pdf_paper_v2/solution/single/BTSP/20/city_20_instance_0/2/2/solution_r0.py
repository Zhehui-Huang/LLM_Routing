import math
import numpy as np
from scipy.spatial.distance import pdist, squareform

# Coordinates of the cities, where the index corresponds to the city number
cities = [
    (8, 11),  # City 0: Depot
    (40, 6),  # City 1
    (95, 33), # City 2, etc.
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

n = len(cities)

# Calculate the Euclidean distances between each pair of cities
def euclidean_dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create a distance matrix
dist_matrix = squareform(pdist(cities, metric='euclidean'))

# Placeholder for TSP solution using a heuristic
def tsp_solution(dist_matrix):
    from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order
    
    # Step 1: Compute the Minimum Spanning Tree
    mst = minimum_spanning_tree(dist_matrix).toarray()
    
    # Step 2: Double tree heuristic for TSP
    tour = []
    visited = [False] * n
    def visit(city):
        visited[city] = True
        tour.append(city)
        for neighbor in range(n):
            if mst[city, neighbor] > 0 and not visited[neighbor]:
                visit(neighbor)
                tour.append(city)  # come back to starting city
        
    visit(0)  # start from the depot
    closed_tour = [tour[0]] + [city for i, city in enumerate(tour) if i == 0 or city != tour[i - 1]]  # remove immediate repeats

    # Step 3: Optimize the tour to remove unnecessary returns to depot if exist
    optimized_tour = []
    for city in closed_tour:
        if city not in optimized_tour:
            optimized_tour.append(city)
    optimized_tour.append(0)  # close the tour at the depot
    
    return optimized_tour

def calculate_tour_details(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = dist_matrix[tour[i], tour[i+1]]
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

# Solve the TSP
tour = tsp_solution(dist_matrix)
total_cost, max_distance = calculate_tour_details(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))