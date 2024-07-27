import numpy as np
from scipy.spatial import distance_matrix

# Define the coordinates of the cities
cities = [
    (8, 11),  # Depot: city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (5, 59), (62, 88), (13, 43), (61, 25), (61, 28), (60, 63), (93, 15)
]

# Compute the distance matrix
dist_matrix = distance_matrix(cities, cities)

# Nearest Neighbor Algorithm
def nearest_neighbor(dist_matrix):
    num_cities = dist_matrix.shape[0]
    visited = np.zeros(num_cities, dtype=bool)
    tour = [0]
    visited[0] = True
    current_city = 0

    while len(tour) < num_cities:
        min_dist = np.inf
        next_city = None
        for city in range(num_cities):
            if not visited[city] and dist_matrix[current_city, city] < min_dist:
                min_dist = dist_matrix[current_city, city]
                next_city = city
        visited[next_city] = True
        tour.append(next_city)
        current_city = next_city
    
    tour.append(0)  # Return to the depot
    return tour

# Calculate the tour using the nearest neighbor heuristic
tour = nearest_neighbor(dist_matrix)

# Calculate the total cost of the tour
total_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)