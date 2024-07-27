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
    # Calculate Euclidean distance between two points (cities).
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix computation
n = len(cities)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

def nearest_neighbor_tour(start=0):
    # Nearest neighbor algorithm to find a path.
    unvisited = list(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # Make sure to return to the starting point
    return tour

# Generate tour using the nearest neighbor approach
tour = nearest_neighbor_tour()

# Calculate total cost and maximum distance between consecutive cities
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the results
output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

# Ensuring the output is printed
print("Tour:", output["Tour"])
print("Total travel cost:", output["Total travel mort"])
print("Maximum distance between consecutive cities:", output["Maximum distance between consecutive cities"])