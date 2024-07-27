import numpy as np
from scipy.spatial import distance_matrix

# Define the coordinates of the cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate distance matrix using Euclidean distance
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

def nearest_neighbor_tsp(start, dist_matrix):
    num_cities = dist_matrix.shape[0]
    unvisited = set(range(num_cities))
    unvisited.remove(start)
    tour = [start]
    current = start
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        total_cost += dist_matrix[current][next_city]
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    # Returning to the starting point
    total_cost += dist_matrix[current][start]
    tour.append(start)

    return tour, total_cost

# Get the tour and cost from the defined start city
tour, total_cost = nearest_neighbor_tsp(0, dist_matrix)

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)