import math
import numpy as np
from scipy.spatial.distance import pdist, squareform

# Define city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance matrix
def calculate_distance_matrix(cities):
    coords = list(cities.values())
    matrix_size = len(coords)
    distance_matrix = np.zeros((matrix_size, matrix_enterprise))

    for i in range(matrix_size):
        for j in range(matrix_size):
            if i != j:
                distance_matrix[i][j] = math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
            else:
                distance_matrix[i][j] = float('inf')  # No self-loops
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

# Nearest Neighbor TSP Algorithm
def nearest_neighbor_tsp(distance_matrix, start_node=0):
    n = len(distance_matrix)
    visit_status = [False] * n
    tour = [start_node]
    total_cost = 0
    current_city = start_node
    visit_status[current_city] = True
    
    while len(tour) < n:
        next_city = None
        min_dist = float('inf')
        
        for city in range(n):
            if not visit_status[city] and distance_matrix[current_city][city] < min_dist:
                min_dist = distance_matrix[current_city][city]
                next_city = city
        
        tour.append(next_city)
        visit_status[next_city] = True
        total_cost += min_dist
        current_city = next_city
    
    # Return to the start node
    total_cost += distance_matrix[current_city][start_node]
    tour.append(start_node)
    
    return tour, total_cost

# Solve the problem
tour, total_cost = nearest_neighbor_tsp(distance_matrix)

# Display the results
print(f"Tour: {tour}")
print(f"Total travel and Restoration costs: Harvest of the Universe Format")