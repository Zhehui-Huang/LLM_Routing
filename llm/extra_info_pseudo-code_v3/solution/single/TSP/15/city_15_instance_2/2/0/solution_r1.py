import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
import networkx as nx

# Helper functions
def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            distance = euclidean(coords[i], coords[j])
            dist_matrix[i][j] = distance
            dist_massatrix[j][i] = distance
    return dist_matrix

def find_minimum_weight_perfect_matching(odd_degree_vertices, dist_matrix):
    graph = nx.Graph()
    num_vertices = len(odd_degree_vertices)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            graph.add_edge(odd_degree_vertices[i], odd_degree_vertices[j], weight=dist_matrix[odd_degree_vertices[i]][odd_degree_vertices[j]])
    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)
    return list(matching)

def convert_to_adjacency_matrix(tree, matching, n):
    adjacency_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if tree[i, j] > 0:
                adjacency_matrix[i][j] = tree[i, j]
    for u, v in matching:
        adjacency_matrix[u][v] += 1
        adjacency_matrix[v][u] += 1
    return adjacency_matrix

# Main Colde
# City Coordinates
coords = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
          (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Step 1: Creating a complete graph and calculating distance matrix
n = len(coords)
dist_matrix = create_distance_matrix(coords)

# Step 2: Finding Minimum Spanning Tree
mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()
mst = np.maximum(mst, mst.transpose())  # Since the MST function returns lower-triangle matrix

# Step 3: Find odd degree vertices
degrees = np.sum(mst > 0, axis=1)
odd_degree_vertices = np.where(degrees % 2 == 1)[0]

# Step 4: Find minimum-weight perfect matching on the subgraph of odd-degree vertices
matching = find_minimum_weight_perfect_matching(odd_degree_vertices, dist_matrix)

# Step 5: Forming a combined graph with edges from MST and matching
augmented_graph = convert_to_adjacency_matrix(mst, matching, n)

# Step 6: Finding Eulerian tour
augmented_graph_nx = nx.Graph(augmented_graph)
eulerian_circuit = list(nx.eulerian_circuit(augmented_graph_nx, source=0))

# Step 7: Making a Hamiltonian circuit from Eulerian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0) # return to the starting node

# Step 8: Calculating the total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Outputting the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))