import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Calculate Euclidean distances between every pair of points
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

# Nearest neighbor TSP algorithm
def nearest_neighbor_tsp(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = [0]
    visited[0] = True
    current_city = 0
    total_cost = 0
    
    while len(tour) < num_cities:
        next_city = None
        min_dist = float('inf')
        for city in range(num_cities):
            if not visited[city] and distances[current_city][city] < min_dist:
                min_dist = distances[current_city][city]
                next_city = city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        current_city = next_city
    
    # Return to the depot city
    total_cost += distances[current_city][0]
    tour.append(0)
    
    return tour, total_cost

# Calculate the distance matrix from the cities
dist_matrix = calculate_distances(cities)

# Solve the TSP
tour, total_cost = nearest_neighbor_tsp(dist_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")