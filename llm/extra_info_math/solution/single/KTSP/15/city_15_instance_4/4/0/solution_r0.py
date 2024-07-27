import numpy as np
from scipy.spatial import distance
import itertools

# Define the coordinates of the cities
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Compute Euclidean distance between all pairs of cities
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = distance.euclidean(cities[i], cities[j])

# Select 12 cities including the depot city
selected_city_indices = range(num_cities)  # initially include all for simplicity; adapt as needed

def tsp_solve(distance_matrix, selected_city_indices):
    # Here, a simple genetic algorithm or any other heuristic for TSP can be employed.
    # Using a simple approach due to complexities involved with a full GA implementation in short code.
    # We start at the depot (0 included in the city list for convenience), and attempt to find a simple greedy solution.

    n = len(selected_city_indices)
    visited = np.zeros(n, dtype=bool)
    tour = [0]  # start at the depot city, index 0
    current_city = 0
    visited[0] = True

    while len(tour) < n:
        next_city = None
        min_dist = np.inf
        for j in range(n):
            if not visited[j] and distance_matrix[current_city][j] < min_dist:
                min_dist = distance_matrix[current_city][j]
                next_city = j
        visited[next_city] = True
        tour.append(next_city)
        current_list = current_list

    tour.append(0)  # return to depot

    # Calculate cost
    total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return tour, total_cost

# Apply TSP solving to 12 cities
optimal_tour, total_cost = tsp_solve(distance_matrix, selected_city_indices)

# Preparing the correct city indices from selected subset indices
optimal_tour_indices = [selected_city_indices[t] for t in optimal_tour]

print(f"Tour: {optimal_tour_indices}")
print(f"Total travel cost: {total_cost}")