import math
import numpy as np
from scipy.spatial.distance import pdist, squareform

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
    9: (13, 17),
}

# Calculate Euclidean distances between all pairs
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, metric='euclidean'))

def create_tour(distances):
    n = len(distances)
    unvisited = list(range(n))
    tour = [0]  # start at the depot
    unvisited.remove(0)

    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distances[last][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    
    tour.append(0)  # end at the depot
    return tour

tour = create_tour(dist_matrix)

def calculate_costs(tour, dist_matrix):
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost, max_distance

total_cost, max_distance = calculate_costs(tour, dist_matrix)

# Output as required
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)