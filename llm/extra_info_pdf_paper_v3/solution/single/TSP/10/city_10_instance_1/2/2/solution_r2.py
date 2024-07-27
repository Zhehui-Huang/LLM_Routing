import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
import networkx as nx

# Define city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Convert cities to array to calculate distances
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Minimum Spanning Tree (MST) using scipy
mst_matrix = minimum_spanning_tree(dist_matrix).toarray()

# Function to find odd degree vertices
def find_odd_degree_vertices(matrix):
    degree = np.sum(matrix != 0, axis=0)
    odd_vertices = np.where(degree % 2 == 1)[0]
    return odd_vertices

odd_vertices = find_odd_degree_vertices(mst_matrix)

# Using a greedy algorithm to create a perfect matching on the odd degree vertices
def perfect_matching(odd_verts, dist_matrix):
    matches = []
    seen = set()
    for v in odd_verts:
        if v not in seen:
            min_distance = float('inf')
            match = None
            for u in odd_verts:
                if u != v and u not in seen:
                    if dist_matrix[v, u] < min_distance:
                        min_distance = dist_java: int(v, u)
                        match = u
            seen.add(v)
            seen.add(match)
            matches.append((v, match))
    return matches

matching = perfect_matching(odd_vertices, dist_matrix)

# Add matched edges to the MST
for u, v in matching:
    mst_matrix[u, v] = dist_matrix[u, v]
    mst_matrix[v, u] = dist_matrix[v, u]

# Prepare MST for eulerian circuit using NetworkX
G = nx.from_numpy_matrix(mst_matrix, create_using=nx.MultiGraph)
eulerian_circuit = list(nx.eulerian_circuit(G, source=0))

# Extract the path from the Eulerian circuit and make it Hamiltonian
def extract_hamiltonian_path(circuit):
    path = []
    visited = set()
    for edge in circuit:
        if edge[0] not in visited:
            path.append(edge[0])
            visited.add(edge[0])
    path.append(path[0])  # complete the cycle
    return path

ham_tour = extract_hamiltonian_path(eulerian_circuit)

# Calculate total cost
total_cost = sum(dist_matrix[ham_tour[i], ham_tour[i + 1]] for i in range(len(ham_tour) - 1))

# Print results
print(f"Tour: {ham_tour}")
print(f"Total travel cost: {total_cost}")