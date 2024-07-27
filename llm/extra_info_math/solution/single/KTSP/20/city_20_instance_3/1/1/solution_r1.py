import numpy as np
import itertools
from scipy.spatial.distance import euclidean
from networkx import Graph, approximation

# Define the cities (Depot + 19 other cities)
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Number of cities to visit including the depot
k = 13

# Compute all pairwise distances
def compute_distances(cities):
    N = len(cities)
    dist_matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

dist_matrix = compute_distances(cities)

# Function to compute the total travel cost of a tour
def total_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Solve k-TSP using a heuristic approach (greedy)
def solve_k_tsp(dist_matrix, k):
    # Create graph from the distance matrix
    G = Graph()
    n = len(dist_matrix)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=dist_matrix[i][j])

    # Explore all combinations to find the minimum tour
    min_tour, min_cost = None, float('inf')
    for subset in itertools.combinations(range(1, n), k - 1):
        nodes = [0] + list(subset)
        subgraph = G.subgraph(nodes)
        # Attempt to find a TSP in the subgraph
        try:
            tour = approximation.traveling_salesman_problem(subgraph, cycle=True, weight='weight')
            cost = total_cost(tour, dist_matrix)
            if cost < min_cost:
                min_tour, min_cost = tour, cost
        except ValueError:
            # Skip iteration if no Hamiltonian cycle could be found
            continue

    # Ensure the tour ends at the starting node
    if min_tour:
        min_tour.append(min_tour[0])
    return min_tour, min_cost

# Solve the k-TSP
tour, cost = solve_k_tsp(dist_matrix, k)

# Ensure results are printed
print("Tour:", tour)
print("Total travel cost:", cost)