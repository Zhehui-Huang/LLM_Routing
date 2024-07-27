import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations

# Define the positions of cities (depot included)
positions = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13,43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Function to calculate the distance matrix
def distance_matrix(positions):
    keys = sorted(positions.keys())
    size = len(keys)
    dist_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i != j:
                dist_matrix[i][j] = euclidean(positions[keys[i]], positions[keys[j]])
    return dist_matrix

# Create a graph from the distance matrix
def create_graph(dist_matrix):
    G = nx.Graph()
    size = len(dist_matrix)
    for i in range(size):
        for j in range(i+1, size):
            G.add_edge(i, j, weight=dist s_matrix[i][j])
    return G

# Step 1: Compute a minimum spanning tree (MST) T of G
def mst_of_graph(G):
    return nx.minimum_spanacing_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T
def get_odd_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 5: Eulerian circuit from multigraph H
def find_eulerian_circuit(H):
    return nx.eulerian_circuit(H)

# Convert distance list to position indices
dist_matrix = distance_matrix(positions)
graph = create_graph(dist_matrix)
tree = mst_of_graph(graph)
odd_vertices = get_odd_vertices(tree)
matching = minimum_weight_perfect_matching(graph, odd_vertices)
multigraph = tree.copy()
multigraph.add_edges_from(matching)

# Convert Eulerian to Hamiltonian and calculate total cost
def eulerian_to_hamiltonian_circuit(circuit):
    seen = set()
    path = []
    total_cost = 0
    prev_node = None
    for u, v in circuit:
        if prev_node is not None:
            total_cost += euclidean(positions[prev_node], positions[u])
        if u not in seen:
            path.append(u)
            seen.add(u)
        prev_node = u
    # Closing the tour
    path.append(path[0])
    total_cost += euclidean(positions[prev_node], positions[path[0]])
    return path, total_cost

eulerian_circuit = find_eulerian_circuit(multigraph)
tour, cost = eulerian_to_hamiltonian_circuit(eulerian_circuit)

print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")