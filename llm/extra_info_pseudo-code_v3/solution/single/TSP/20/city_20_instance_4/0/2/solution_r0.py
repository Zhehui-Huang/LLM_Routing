import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations

def create_complete_graph(coords):
    G = nx.Graph()
    G.add_nodes_from(range(len(coords)))
    distances = distance_matrix(coords, coords)
    for (i, j) in combinations(range(len(coords)), 2):
        G.add_edge(i, j, weight=distances[i][j])
    return G

def find_mst(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def find_odd_degree_vertices(T):
    return [v for v in T.nodes() if T.degree(v) % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, True, 'weight')

def eulerian_circuit(H):
    return list(nx.eulerian_circuit(H, source=0))

def create_hamiltonian_circuit(circuit, start_node):
    visited = {start_node}
    path = [start_node]
    cost = 0

    for u, v in circuit:
        if v not in visited:
            visited.add(v)
            cost += nx.dijkstra_path_length(H, u, v, 'weight')
            path.append(v)

    # adding the return to the start node cost
    final_leg = nx.dijkstra_path_length(H, path[-1], start_node, 'weight')
    path.append(start_node)
    cost += final_leg
    return path, cost

# Coordinates of the cities
coords = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
          (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
          (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Step 1: Create complete graph G
G = create_complete_graph(coords)

# Step 2: Compute the minimum spanning tree (MST) T
T = find_mst(G)

# Step 3: Identify the set O of vertices with odd degree in T
O = find_odd_degree_vertices(T)

# Step 4: Find a minimum-weight perfect matching M in the subgraph induced by O
M = minimum_weight_perfect_matching(G, O)

# Step 5: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 6: Find an Eulerian circuit in multigraph H
circuit = eulerian_circuit(H)

# Step 7: Convert the Eulerian circuit to a Hamiltonian circuit
tour, total_cost = create_hamiltonian_circuit(circuit, 0)

# Output the tour and the total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)