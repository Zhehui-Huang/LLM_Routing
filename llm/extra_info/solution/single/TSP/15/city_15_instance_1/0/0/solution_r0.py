import math
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Function to calculate Euclidean distance matrix
def calculate_distance_matrix(cities):
    points = [cities[i] for i in range(len(cities))]
    return distance_matrix(points, points)

# Calculate TSP tour using a heuristic method
def solve_tsp(distances):
    # We use a minimum-cost perfect matching or Min-Cost Hungarian algorithm for approximation
    row_ind, col_ind = linear_sum_assignment(distances)
    tour = [0]  # Start from depot city 0
    # Since we are considering an asymmetric solution use linear sum assignment twice
    for start, end in zip(row_ind, col_ind):
        if start == 0 or end == 0:
            if start == 0 and end != 0:
                tour.append(end)
            elif start != 0 and end == 0:
                tour.append(start)
    total_cost = sum(distances[row_ind[i], col_ind[i]] for i in range(len(row_ind)))
    tour.append(0)  # Return to depot
    return tour, total_cost

# Calculate distances
dist_matrix = calculate_distance_matrix(cities)

# Solve TSP
tsp_tour, total_tsp_cost = solve_tsp(dist_matrix)

# Output
print(f"Tour: {tsp_tour}")
print(f"Total travel cost: {total_tsp_cost}")