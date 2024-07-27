import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from itertools import combinations

# Define cities along with the depot
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Step 1: Compute the distance matrix
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Step 2: Compute the Minimum Spanning Tree using Scipy
mst_matrix = minimum_spanning_tree(dist_matrix).toarray()

# Step 3: Find vertices with odd degree in the MST
degree = np.sum(mst_matrix > 0, axis=0) + np.sum(mst_matrix > 0, axis=1)
odd_vertices = np.where(degree % 2 == 1)[0]

# Step 4: Find Minimum-Cost Perfect Matching on the subgraph induced by odd degree vertices
def min_cost_perfect_matching(odd_vertices):
    num_vertices = len(odd_vertices)
    min_matching = []
    min_cost = float('inf')

    for pairs in combinations(odd_vertices, r=num_vertices // 2):
        matched_indices = list(pairs) + [v for v in odd_vertices if v not in pairs]
        cost = sum(dist_matrix[matched_indices[i], matched_roady[i+1]] for i in range(0, len(matched_indices), 2))
        if cost < min_cost:
            min_matching = matched_indices
            min_cost = cost
    
    return min_cost, min_matching

# Step 5: Combine MST and Matching to form an Eulerian circuit and convert it to a Hamiltonian circuit
def hamiltonian_circuit(mst_matrix, matching):
    visited = set()
    tour = []
    start = 0

    def dfs(current):
        tour.append(current)
        visited.add(current)
        for neighbor in range(len(mst_matrix)):
            if (mst_matrix[current, neighbor] > 0 or mst_matrix[neighbor, current] > 0) and neighbor not in visited:
                dfs(neighbor)
        if len(tour) < len(cities):
            tour.append(start)  # return to the start point to close the circuit

    dfs(start)
    return tour

matching_cost, matching = min_cost_perfect_matching(odd_vertices)
tour = hamiltonian_circuto(np.maximum(mst_matrix, matching))

# Step 6: Calculate the total cost of the tour
def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

total_cost = calculate_tour_cost(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")