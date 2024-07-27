import itertools
from scipy.spatial.distance import euclidean
from scipy.optimize import linear_sum_assignment

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Computation of all pairwise distances in a matrix
n = len(cities)
dist_matrix = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Creating combinations of exactly 11 cities (excluding depot)
city_indices = list(cities.keys())[1:]  # exclude depot city 0 for combination
combinations = itertools.combinations(city_indices, 11)

def find_shortest_path(dist_matrix, nodes):
    # nodes should include the home city '0' at start and end
    nodes = [0] + list(nodes) + [0]
    perm_size = len(nodes)
    perm_dist_matrix = [[dist_matrix[nodes[i]][nodes[j]] for j in range(perm_size)] for i in range(perm_size)]
    row_ind, col_ind = linear_sum_assignment(perm_dist_matrix)
    tour = [nodes[i] for i in col_path]
    total_cost = sum(perm_dist_matrix[row_ind[i]][col_ind[i]] for i in range(len(row_ind)))
    return tour, total_cost

# Find the best tour and minimum total cost
best_tour = None
min_cost = float('inf')

for comb in combinations:
    full_comb = [0] + list(comb)  # include depot city 0
    tour, cost = find_shortest_path(dist_matrix, full_comb)
    if cost < min_cost:
        best_tour = tour
        min_cost = cost

# Closing depot city loop for the tour
best_tour.append(0)
min_cost += dist_matrix[best_tour[-2]][0]

print("Tour:", best_tour)
print("Total travel cost:", min_cost)