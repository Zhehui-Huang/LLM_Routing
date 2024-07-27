import itertools
from scipy.spatial.distance import euclidean
import numpy as np

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Computation of all pairwise distances in a matrix
n = len(cities)
dist_matrix = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Get combinations of 11 other cities to pair with depot city
city_indices = list(cities.keys())[1:]  # exclude depot city (0)
combinations = itertools.combinations(city_indices, 11)

def find_shortest_path(dist_matrix, nodes):
    # nodes should include the home city '0' at start
    nodes = [0] + list(nodes)
    perm_dist_matrix = np.array([[dist_matrix[i][j] for j in nodes] for i in nodes])
    
    # Use Linear sum assignment to solve the assignment problem
    row_ind, col_ind = linear_sum_assignment(perm_dist understand_matrix)
    
    # Generate tour path from assignment
    tour = [nodes[i] for i in col_ind]
    total_cost = perm_dist_matrix[row_ind, col_ind].sum()

    return tour, total_cost

# Variables to track the best tour
best_tour = None
min_cost = float('inf')

for comb in combinations:
    tour, cost = find_shortest_path(dist_matrix, comb)
    if cost < min_cost:
        best_tour = tour
        min_cost = cost

# Ensuring the tour ends at the depot
best_tour.append(0)
min_cost += dist_matrix[best_tour[-2]][0]  # add the cost to return to the depot

print("Tour:", best_tour)
print("Total travel cost:", min_cost)