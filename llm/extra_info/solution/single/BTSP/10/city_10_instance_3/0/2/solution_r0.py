import numpy as np
from scipy.spatial.distance import euclidean
from heapq import heappop, heappush

# Cities coordinates
cities = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28),
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Number of cities
n = len(cities)

# Compute distance matrix
distance_matrix = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

def find_minimax_tour():
    # Use a simple heuristic for initial simplification: nearest neighbor
    current = 0
    visit_order = [0]
    visited = set(visit_order)
    max_distance_between_consecutive_cities = 0

    while len(visit_order) < n:
        nearest = None
        for i in range(n):
            if i not in visited:
                if nearest is None or distance_matrix[current][i] < distance_matrix[current][nearest]:
                    nearest = i
        visited.add(nearest)
        visit_order.append(nearest)
        max_distance_between_consecutive_cities = max(max_distance_between_consecutive_cities, distance_matrix[current][nearest])
        current = nearest
    
    # Close loop to the depot
    visit_order.append(0)
    max_distance_between_consecutive_cities = max(max_distance_between_consecutive_cities, distance_matrix[current][0])

    # Calculate total cost
    total_cost = sum(distance_matrix[visit_order[i]][visit_order[i + 1]] for i in range(len(visit_order) - 1))

    return visit_order, total_cost, max_distance_between_consecutive_cities

# Using the function to find the tour
tour, total_cost, max_distance = find_minimax_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")