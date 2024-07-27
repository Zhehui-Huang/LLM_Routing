import math
import itertools

# Define city coordinates where the index is the city number
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Compute the distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Heuristic for tour construction minimizing the max segment length
from heapq import heappush, heappop

def min_max_tour(start, n, distance_matrix):
    remaining = set(range(1, n))
    tour = [start]
    current_city = start

    # We simulate an infinite distance to start with
    max_edge = 0

    while remaining:
        next_city = min(remaining, key=lambda x: distance_matrix[current_city][x])
        max_edge = max(max_edge, distance_matrix[current_city][next_city])
        tour.append(next_city)
        current_city = next_city
        remaining.remove(next_city)

    # Return back to the start city
    max_edge = max(max_edge, distance_matrix[current_city][start])
    tour.append(start)

    # Compute total cost
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return tour, total_cost, max_edge

tour, total_cost, max_distance = min_max_tour(0, n, distance_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))