import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Cities and their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 6: (79, 77),
    7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 12: (3, 21),
    13: (60, 55), 14: (4, 39)
}

# Compute the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a complete graph with weights equal to Euclidean distances
def create_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean_distance(cities[i], cities[j])
            dist_matrix[i, j] = dist
            dist_matrix[j, i] = dist
    
    return dist_matrix

# Christofides algorithm steps
def christofides_algorithm(cities):
    num_cities = len(cities)
    dist_matrix = create_distance_matrix(cities)
    G = csr_matrix(dist_matrix)

    # 1. Compute a minimum spanning tree T of G
    Tcsr = minimum_spanning_tree(G)
    T = Tcsr.toarray().astype(float)
    
    # Create a graph from the MST
    MST_graph = nx.Graph()
    for i in range(num_cities):
        for j in range(num_cities):
            if T[i, j] > 0:
                MST_graph.add_edge(i, j, weight=T[i, j])

    # 2. Identify the set O of vertices with odd degree in T
    odd_vertices = [v for v, d in MST_graph.degree() if d % 2 == 1]

    # 3. Find a minimum-weight perfect matching M in the subgraph induced by O
    subgraph = nx.Graph(MST_graph.subgraph(odd_vertices))
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, True)

    # 4. Combine the edges of T and M to form a multigraph H
    multigraph = nx.MultiGraph(MST_graph)
    for u, v in min_weight_matching:
        multigraph.add_edge(u, v)

    # 5. Find an Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))

    # 6. Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    if path[0] != 0:  # ensuring we start at the depot city
        path = [0] + path
    if path[-1] != 0:
        path.append(0)  # ensuring we end at the depot city

    # Calculate the total travel cost
    total_cost = sum(dist_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))

    return path, total_cost

# Find the tour and the total cost
tour, cost = christofides_algorithm(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", cost)