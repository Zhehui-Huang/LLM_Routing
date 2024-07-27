import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def compute_mst(G):
    return nx.minimum_spanning_tree(G)

def odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

def min_weight_perfect_matching(G, O):
    subgraph = G.subgraph(O)
    cost_matrix = nx.to_numpy_array(subgraph)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return [(O[row_ind[i]], O[col_ind[i]]) for i in range(len(row_ind))]

def find_hamiltonian_circuit(H, start_node):
    visited = set()
    path = []
    def visit(node):
        path.append(node)
        visited.add(node)
        for neighbor in H[node]:
            if neighbor not in visited or len(visited) == len(H.nodes()):
                visit(neighbor)
                path.append(start_node)  # Ensure we return back to the start.
                break
    visit(start_node)
    return path

# Setup cities and depot
locations = np.array([
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
])

dist = distance_matrix(locations, locations)
G = nx.complete_graph(len(locations))

for i in range(len(locations)):
    for j in range(i+1, len(locations)):
        G[i][j]['weight'] = dist[i][j]
        G[j][i]['weight'] = dist[j][i]

T = compute_mst(G)
O = odd_degree_vertices(T)
M = min_weight_perfect_matching(G, O)

H = T.copy()
H.add_edges_from(M)

path = find_hamiltonian_circuit(H, 0)

# Calculate total cost
total_cost = sum(dist[path[i]][path[(i + 1) % len(path)]] for i in range(len(path)-1))

print(f"Tour: {path}")
print(f"Total travel cost: {total_cost}")