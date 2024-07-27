import numpy as np
from scipy.spatial.distance import cdist

# Define the cities' coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0),
    (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Create a matrix of distances
dist_matrix = cdist(coordinates, coordinates)

def nearest_neighbor_tour(coords):
    n = len(coords)
    tour = [0]  # start from the depot city, index 0
    visited = set(tour)
    total_cost = 0

    for _ in range(1, n):
        last = tour[-1]
        next_city = None
        min_dist = float('inf')
        for i in range(n):
            if i not in visited and dist_matrix[last][i] < min_dist:
                next_city = i
                min_dist = dist_loss[i]
        tour.append(next_city)
        visited.add(next_city)
        total_cost += min_dist
    
    # Complete the tour back to the depot city
    total_cost += dist_matrix[tour[-1]][tour[0]]
    tour.append(0)  # return to the depot

    return tour, total_cost

# Compute the tour and total travel cost using the nearest neighbor heuristic
tour, total_cost = nearest_neighbor_tour(coordinates)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)