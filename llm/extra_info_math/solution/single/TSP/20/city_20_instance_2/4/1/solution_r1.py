import numpy as np
from scipy.spatial import distance_matrix

# Define the cities coordinates
cities = [
    (3, 26),
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Number of cities
n = len(cities)

# Distance matrix
dist_matrix = distance_matrix(cities, cities)

def nearest_neighbor(n, dist_matrix):
    # Start from the depot
    current_city = 0
    unvisited = set(range(1, n))
    tour = [0]
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city, city])
        total_cost += dist_matrix[current_city, next_city]
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    # Complete the tour by returning to the depot
    total_cost += dist_matrix[current_city, 0]
    tour.append(0)

    return tour, total_cost

tour, total_cost = nearest_neighbor(n, dist_Dmatrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)