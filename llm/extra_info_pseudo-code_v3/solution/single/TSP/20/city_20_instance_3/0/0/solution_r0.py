import numpy as np
from scipy.spatial.distance import euclidean
from heapq import heappop, heappush
from networkx import Graph, minimum_spanning_tree, eulerian_circuit, is_eulerian
from networkx.algorithms.matching import min_weight_matching

def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean(cities[i], cities[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
            
    return dist_matrix

def prim_mst(dist_matrix):
    num_cities = len(dist_matrix)
    in_mst = [False] * num_cities
    min_edge = [(0, 0)]  # (cost, vertex)
    mst_edges = []
    
    while len(mst_edges) < num_cities:
        cost, v = heappop(min_edge)
        if in_mst[v]:
            continue
            
        in_mst[v] = True
        for u, dist in enumerate(dist_matrix[v]):
            if not in_mst[u]:
                heappush(min_edge, (dist, u))
        
        if v != 0:  # Prevents the dummy edge (0, 0) from being added to the list
            mst_edges.append((cost, v))
            
    return mst_edges

def add_mst_edges(G, mst_edges):
    for cost, v in mst_edges:
        np, dp = divmod(v, len(G))
        G.add_edge(np, dp, weight=cost)

def create_graph_with_mst(dist_matrix, mst_edges):
    G = Graph()
    n = len(dist_matrix)
    G.add_nodes_from(range(n))
    
    for cost, (i, j) in mst_edges:
        G.add_edge(i, j, weight=cost)
        
    return G

def christofides_algorithm(cities):
    dist_matrix = calculate_distances(cities)
    mst_edges = prim_mst(dist_matrix)
    G = create_graph_with_mst(dist_matrix, mst_edges)
    
    odd_degree_nodes = [v for v in G if G.degree(v) % 2 == 1]
    min_weight_subgraph = G.subgraph(odd_degree_nodes)
    matching_edges = min_weight_matching(min_weight_subgraph, True, "weight")
    G.add_edges_from(matching_edges)
    
    # Ensure the graph is Eulerian
    assert is_eulerian(G), "Graph should be Eulerian by now"
    
    euler_circuit = list(eulerian_circuit(G))
    
    # Transform Eulerian into Hamiltonian
    visited = set()
    hamiltonian_cycle = [0]
    total_distance = 0
    current_node = 0
    
    for u, v in euler_circuit:
        if v not in visited:
            hamiltonian_cycle.append(v)
            total_distance += dist_matrix[current_node][v]
            visited.add(v)
            current_node = v
            
    # Add return to start
    hamiltonian_cycle.append(0)
    total_distance += dist_matrix[current_node][0]
    
    return hamiltonian_cycle, total_distance

# Define cities coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Execute Christofides algorithm
tour, total_cost = christofides_algorithm(cities)

# Print the final output
print("Tour:", tour)
print("Total travel cost:", total_cost)