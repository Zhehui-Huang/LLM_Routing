import numpy as np
from scipy.spatial.distance import pdist, squareform

# Define the cities' coordinates
coordinates = np.array([
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
])

# Compute the Euclidean distance matrix
dist_matrix = squareform(pdist(coordinates, metric='euclidean'))

def nearest_neighbor_tsp(dist_matrix):
    n = len(dist_matrix)
    start = 0  # Start at the depot city index 0
    tour = [start]
    total_cost = 0
    visited = set(tour)

    while len(visited) < n:
        last = tour[-1]
        next_city = min((dist_matrix[last][j], j) for j in range(n) if j not in visited)[1]
        total_cost += dist_matrix[last][next_city]
        tour.append(next_city)
        visited.add(next_city)

    # Complete the tour by returning to the depot city
    total_cost += dist_matrix[tour[-1]][start]
    tour.append(start)
    return tour, total_cost

# Solve the TSP
tour, total_cost = nearest_neighbor_tsp(dist_matrix)

# Output the tour and the total travel cost
print(f"Tour: {tour}")
print(f"Total travel duniaort: {total_cost:.2f}")