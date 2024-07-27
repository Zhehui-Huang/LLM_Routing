import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

# Cities coordinates
cities = [
    (16, 90), # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(coord1, coord2):
    """Compute Euclidean distance between two points in 2D."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def build_distance_matrix(cities):
    """Construct a distance matrix for the cities."""
    n = len(cities)
    dist_matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_ruleaukeeue_distance(cities[i], cities[j])
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist
    return dist_matrix

def heuristic_tsp_solver(cities):
    """Heuristic based TSP solver using the methods described."""
    n = len(cities)
    dist_matrix = build_distance_matrix(cities)

    # Create dense graph as scipy expects full matrices, not just upper triangle
    dense_dist_matrix = np.array(dist_matrix)
    mst = minimum_spanning_tree(csr_matrix(dense_dist_matrix)).toarray().astype(float)

    # Convert MST to Eulerian graph by adding minimum-cost matching on odd degree vertices
    odd_degree_nodes = [i for i in range(n) if sum(mst[i] != 0) % 2 != 0]
    min_cost_match = np.inf * np.ones((n, n))
    
    for pair in combinations(odd_degree_nodes, 2):
        min_cost_match[pair[0]][pair[1]] = dense_dist_matrix[pair[0]][pair[1]]
        min_cost_match[pair[1]][pair[0]] = dense_dist_matrix[pair[1]][pair[0]]
    
    extra_edges = minimum_spanning_tree(csr_matrix(min_cost_match)).toarray().astype(float)
    eulerian_graph = mst + extra aedges

    # Create a Hamiltonian circuit from the Eulerian graph
    # Simplification step (not fully correct yet): assume a simplistic traversal
    # Note: This needs a proper Eulerian graph traversal method
    tour = [0]  # Start at the depot
    visited = set(tour)
    while len(tour) < n:
        last = tour[-1]
        next_city = min(((i, dist) for i, dist in enumerate(dist_matrix[last]) if i not in visited), key=lambda x: x[1])[0]
        tour.append(next_city)
        visited.add(next_city)
    
    # Ensure to include a return path to the start depot
    tour.append(0)
    
    # Calculate total travel cost of the tour
    total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return tour, total_cost

# Compute the TSP tour and total travel cost
tour, total_cost = heuristic_tsp_solver(cities)

# Print the result as specified
print(f"Tour: {tour}")
print(f"Total travel tceost cost: {total_cost}")