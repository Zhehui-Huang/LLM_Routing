import networkx as nx
import numpy as np
from scipy.spatial import distance
from networkx.algorithms import approximation as approx
from networkx.algorithms import eulerian_circuit

# City coordinates
coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Compute the Euclidean distance matrix
def euclidean_distance_matrix(coords):
    return distance.cdist(coords, coords, 'euclidean')

dist_matrix = euclidean_distance_matrix(coords)

# Create a complete graph from the distance matrix
def create_graph(dist_matrix):
    G = nx.Graph()
    for i in range(len(dist_matrix)):
        for j in range(i + 1, len(dist_matrix)):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

G = create_graph(dist_matrix)

# 1. Compute a minimum spanning tree (MST) of G
mst = nx.minimum_spanning_tree(G)

# 2. Identify the set of vertices with odd degree in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# 3. Find a minimum-weight perfect matching in the subgraph induced by the odd-degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = approx.min_weight_matching(odd_subgraph, True)

# 4. Add the edges of the minimum weight perfect matching to the MST
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# 5. Find an Eulerian circuit in the multigraph
euler_circuit = list(eulerian_circuit(multi_graph))

# 6. Convert the Eulerian circuit to a Hamiltonian circuit (skip repeated vertices)
def create_hamiltonian_circuit(euler_circuit):
    seen = set()
    path = []
    path_cost = 0
    last = None
    for (u, v) in euler_circuit:
        if u not in seen:
            path.append(u)
            seen.add(u)
        if last is not None:
            path_cost += dist_matrix[last][u]
        last = u
    path.append(path[0])  # close the tour
    path_cost += dist_matrix[path[-2]][path[-1]]
    return path, path_cost

tour, total_cost = create_hamiltonian_circuit(euler_circuit)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))