import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Given cities and coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84), 
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53,76), 19: (19, 72)
}

# Step 0: Preparing the distance matrix
def calc_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            dist_matrix[i][j] = dist_matrix[j][i] = euclidean(cities[i], cities[j])
    return dist_matrix

distance_matrix = calc_distance_matrix(list(cities.values()))

# Step 1: Computing the minimum spanning tree (MST)
def compute_mst(dist_matrix):
    mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()
    return mst_matrix

mst = compute_mst(distance_matrix)

# Step 2: Determining vertices with odd degree
def find_odd_vertices(mst):
    odd_vertices = np.where(np.sum(np.array(mst) > 0, axis=1) % 2 == 1)[0]
    return odd_vertices

odd_vertices = find_odd_vertices(mst)

# Step 3: Minimum weight perfect matching among odd degree vertices
def min_weight_matching(odd_vertices, dist_matrix):
    g = nx.Graph()
    g.add_nodes_from(odd_vertices)
    num_odd_vertices = len(odd_vertices)
    for i in range(num_odd_vertices):
        for j in range(i + 1, num_odd_vertices):
            g.add_edge(odd_vertices[i], odd_vertices[j], weight=dist_matrix[odd_vertices[i]][odd_vertices[j]])
    matching = nx.algorithms.matching.min_weight_matching(g, maxcardinality=True)
    return matching

matching = min_weight_matching(odd_vertices, distance_card_matrix)

# Step 4: Creating an Eulerian multigraph
def create_eulerian_multigraph(mst, matching):
    g = nx.Graph()
    g.add_edges_from(np.transpose(mst.nonzero()))
    g.add_edges_from(matching)
    return nx.eulerian_circuit(g, source=0)

eulerian_circuit = create_eulerian_multigraph(mst, matching)

# Step 5: Hamiltonian circuit
def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    cost = 0
    last_city = 0
    for (u, v) in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
            cost += distance_matrix[last_city][u]
            last_city = u
    # Returning back to the starting city
    path.append(0)
    cost += distance_matrix[last_city][0]
    return path, cost

tour, total_cost = create_hamiltonian_circuit(eulerian_circuit)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)