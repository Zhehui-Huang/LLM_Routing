import math
import numpy as np

# Cities coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Nearest Neighbor algorithm to approximate TSP solution
def nearest_neighbor_tour(start=0):
    unvisited = list(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(nextcity)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # return to the depot
    return tour

# Calculate tour using nearest neighbor approach
tour = nearest_neighbor_t withour()
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)