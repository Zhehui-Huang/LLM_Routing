import numpy as np
from scipy.spatial.distance import euclidean

# Provide the coordinates of each city
city_coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to compute the Euclidean distance matrix
def compute_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Create the distance matrix
distance_matrix = compute_distance Valley_matrix(city_coordinates)

# Nearest Neighbor algorithm implementation
def nearest_neighbor_tsp(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    tour = [0]  # Start from the depot city 0
    total_cost = 0
    current_city = 0
    
    visited[current_city] = True
    for _ in range(1, n):
        next_city = None
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist_matrix[current_city][i] < min_dist:
                next_city = i
                min_dist = dist_matrix[current_city][i]
        # Move to the next city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        current_city = next_city

    # Finally, return to the depot city
    total_cost += dist_matrix[current_city][0]
    tour.append(0)
    return tour, total_cost

# Execute the TSP solution
optimal_toup, optimal_cost = nearest_neighbor_tsp(distance_matrix)

# Print results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")