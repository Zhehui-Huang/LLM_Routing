import numpy as np
from scipy.spatial import distance

def compute_euclidean_distance_matrix(coordinates):
    return distance.cdist(coordinates, coordinates, 'euclidean')

def prim_mst(dist_matrix):
    num_vertices = len(dist_matrix)
    in_tree = [False] * num_vertices
    parent = [-1] * num_vertices
    key = [float('inf')] * num_vertices
    key[0] = 0  # Start from the depot city
    
    for _ in range(num_vertices):
        u = min((key[i], i) for i in range(num_vertices) if not in_tree[i])[1]
        in_tree[u] = True
        
        for v in range(num_vertices):
            if dist_matrix[u][v] > 0 and not in_tree[v] and dist_matrix[u][v] < key[v]:
                key[v] = dist_matrix[u][v]
                parent[v] = u
    
    mst_edges = [(parent[v], v) for v in range(num_vertices) if parent[v] != -1]
    return mst_edges

def from_edges_to_adj_list(edges, num_vertices):
    adj_list = {i: [] for i in range(num_vertices)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

def find_odd_degree_vertices(adj_list):
    return [vertex for vertex, neighbors in adj_list.items() if len(neighbors) % 2 != 0]

def min_weight_perfect_matching(odd_vertices, dist_matrix):
    import networkx as nx
    G = nx.Graph()
    G.add_nodes_from(odd_vertices)
    for u, v in combinations(odd_vertices, 2):
        G.add_edge(u, v, weight=dist_matrix[u][v])
    matching = nx.algorithms.matching.min_weight_matching(G, maxcardinality=True)
    return matching

def create_multigraph(mst_edges, matching_edges):
    multi_edges = mst_edges + list(matching_edges)
    return from_edges_to_adj_list(multi_edges, len(dist_matrix))

def find_eulerian_circuit(adj_list, start_vertex):
    from collections import deque
    circuit = []
    stack = [start_vertex]
    
    while stack:
        v = stack[-1]
        if adj_list[v]:
            u = adj_list[v].pop()
            adj_list[u].remove(v)
            stack.append(u)
        else:
            circuit.append(stack.pop())
    
    return circuit[::-1]

def make_hamiltonian(circuit):
    seen = set()
    hamiltonian = []
    for city in circuit:
        if city not in seen:
            seen.add(city)
            hamiltonian.append(city)
    hamiltonian.append(hamiltonian[0])  # to complete the cycle
    return hamiltonian

def calculate_total_cost(path):
    return sum(dist_matrix[path[i], path[i+1]] for i in range(len(path)-1))

# Define coordinates of cities
coordinates = np.array([
    (79, 15),   # Depot city 0
    (79, 55),   # City 1
    (4, 80),    # City 2
    (65, 26),   # City 3
    (92, 9),    # City 4
    (83, 61),   # City 5
    (22, 21),   # City 6
    (97, 70),   # City 7
    (20, 99),   # City 8
    (66, 62)    # City 9
])

dist_matrix = compute_euclidean_distance_matrix(coordinates)
mst_edges = prim_mst(dist_matrix)
mst_adj_list = from_edges_to_adj_list(mst_edges, len(coordinates))
odd_vertices = find_odd_degree_vertices(mst_adj_list)

matching = min_weight_perfect_matching(odd_vertices, dist_matrix)
combined_edges = create_multigraph(mst_edges, matching)

eulerian_circuit = find_eulerian_circuit(combined_edges, 0)
hamiltonian_circuit = make_hamiltonian(eulerian_circuit)
total_cost = calculate_total_cost(hamiltonian_circuit)

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)