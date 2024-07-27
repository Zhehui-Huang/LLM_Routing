import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import linear_sum_assignment

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Given city coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Convert city coordinates to list for efficient processing
city_locations = [cities[k] for k in sorted(cities)]

# Compute the distance matrix
dist_matrix = pdist(city_locations)
dist_matrix = squareform(dist_matrix)

# For making the matrix symmetric
np.fill_diagonal(dist_matrix, 0)

# Apply Lin-Kernighan like approach using the Hungarian or Munkres algorithm
def solve_tsp(dist_matrix):
    # Approximation: convert to a linear assignment problem
    row_ind, col_ind = linear_sum_assignment(dist_matrix)
    tour = list(row_ind)
    total_cost = dist_matrix[row_ind, col_ind].sum()
    return tour, total_cost

# Get initial tour and cost
initial_tour, initial_cost = solve_tsp(dist_matrix)

# As cities are only required visited once and return to depot city
tour = [0]
visited = set()
current = 0
total_travel_cost = 0

for next_city in initial_tour:
    if next_city != 0 and next_city not in visited:
        tour.append(next_city)
        total_travel_data += dist_matrix[current, next_city]
        visited.add(next_city)
        current = next_city

# Return to depot
tour.append(0)
total_travel_cost += dist_matrix[current, 0]

# Output the results
print("Tour: ", tour)
print("Total travel cost: ", round(total_travel_cost, 2))