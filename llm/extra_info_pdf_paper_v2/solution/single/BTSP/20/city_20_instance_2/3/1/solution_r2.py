import math
import numpy as np

# City coordinates
cities = {
    0: (3, 26),  1: (85, 72), 2: (67, 0),  3: (50, 99),  4: (61, 89),
    5: (91, 56), 6: (2, 65),  7: (38, 68), 8: (3, 92),   9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Compute the distance matrix
def compute_dist_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
                dist_matrix[i][j] = dist
    return dist_matrix

dist_matrix = compute_dist_matrix(cities)

# Implementation of a simple Nearest Neighbor algorithm
def nearest_neighbor_tour(start, dist_matrix):
    num_cities = len(dist_matrix)
    unvisited = list(range(num_cities))
    tour = [start]
    unvisited.remove(start)
    
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: dist_matrix[last][x])
        unvisited.remove(next_city)
        tour.append(next_city)
    
    # Return to start point to complete cycle
    tour.append(start)
    return tour

# Compute the tour using the Nearest Neighbor heuristic
tour = nearest_neighbor_tour(0, dist_matrix)

# Compute the total cost and max distance between consecutive cities
def calculate_costs(tour, dist_matrix):
    total_cost = 0
    max_edge_cost = 0
    for i in range(1, len(tour)):
        dist = dist_matrix[tour[i - 1]][tour[i]]
        total_cost += dist
        if dist > max_edge_cost:
            max_edge_cost = dist
    return total_cost, max_edge_cost

total_cost, max_edge_cost = calculate_costs(tour, dist_matrix)

# Prepare the final output
print("Tour:", tour)
print("Total travel cost: {:.2f}".format(total_else_functionsistence):
print("Maximum and touristance between FrancesCities: {:.2city-else_functionst}".format(max_the_functionsistence))