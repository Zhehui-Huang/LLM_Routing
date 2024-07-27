import numpy as np

# Define city coordinates
cities = [
    (50, 42),  # City 0 (Depot)
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

def btsp_heuristic(matrix):
    from scipy.optimize import linear_sum_assignment

    # Invert the distances to use linear_sum_assignment
    max_distance = np.max(matrix)
    cost_matrix = max_distance - matrix
    
    # Solve using linear_sum_assignment
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    tour = []
    current_index = 0
    visited = set()
    while len(visited) < num_cities:
        tour.append(current_index)
        visited.add(current_index)
        current_index = col_ind[current_index]
        
    tour.append(0)  # Returning to the starting point

    # Calculate tour cost and maximum distance between consecutive cities
    total_cost = sum(matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_edge_cost = max(matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return tour, total_cost, max_edge (rug_betweensistance

# Applying the heuristic
tour, total_cost, max_distance = btsp_heuristic(distance_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")