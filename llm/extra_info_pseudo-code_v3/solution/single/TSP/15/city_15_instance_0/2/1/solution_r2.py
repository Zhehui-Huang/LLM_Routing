import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from networkx.algorithms.approximation import min_weighted_dominating_set

def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

def create_complete_graph(dist_matrix):
    G = nx.Graph()
    for i in range(len(dist_list)):
        for j in range(len(dist_list)):
            if i != j:
                G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

def find_tour(coords):
    dist_matrix = calculate_distance_matrix(coords)
    G = create_complete_graph(dist_matrix)

    # Step 1: Minimum Spanning Tree
    mst = tree.minimum_spanning_tree(G, weight='weight')
    
    # Step 2: Vertices with odd degree
    odd_degree_nodes = [v for v, d in mst.degree if d % 2 == 1]
    
    # Step 3: Minimum Weight Perfect Matching on the subgraph induced by odd degree vertices
    odd_subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = matching.min_weight_matching(odd_subgraph, maxcardinality=True)

    # Step 4+5: Create multigraph by combining edges from MST and minimum weight matching
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(min_weight_matching)
    
    # Finding Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))
    
    # Step 6: Make Hamiltonian cycle (skip repeated nodes)
    visited = set()
    tour = []
    for u, v in eulerian_circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
    tour.append(tour[0])  # return to starting node
    
    # Calculate total travel cost
    total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return tour, total_cost

coords = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

tour, total_cost = find_tour(coords)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")