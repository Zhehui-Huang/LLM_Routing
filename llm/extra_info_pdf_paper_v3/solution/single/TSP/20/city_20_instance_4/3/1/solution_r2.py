import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Calculation of the Euclidean distances
def euclidean_distances(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in cities:
        for j in cities:
            if i != j:
                dist_matrix[i][j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
    return dist_matrix

# Create distance matrix
dist_matrix = euclidean_distances(cities)

# Create a complete graph
G = nx.complete_graph(len(cities))
for i in range(len(dist_matrix)):
    for j in range(len(dist_matrix)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Construct MST
T = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree
odd_degree_nodes = [v for v, d in T.degree() if d % 2 != 0]

# Create subgraph of vertices with odd degree
subG = G.subgraph(odd_degree_nodes)

# Minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(subG, maxcardinality=True, weight='weight')
T.add_edges_from(matching)

# Make sure the graph has an Eulerian circuit
assert nx.is_eulerian(T)

# Find the Eulerian circuit
eulerian_tour = list(nx.eulerian_circuit(T, source=0))

# Create a Hamiltonian circuit by skipping repeated nodes
visited = set()
tour = []
for u, v in eulerian_tour:
    if u not in visited:
        tour.append(u)
        visited.add(u)
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(tour[0])  # Return to depot

# Calculate total travel cost
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Print the solution
print("Tour:", tour)
print("Total travel cost:", total_cost)