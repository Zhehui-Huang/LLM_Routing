import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order
import networkx as nx

def calculate_distance_matrix(coordinates):
    return squareform(pdist(coordinates))

def minimum_weight_perfect_matching(G, odd_vertices):
    min_weight_match = nx.Graph()
    min_weight_match.add_nodes_from(odd_vertices)
    for i in odd_vertices:
        for j in odd_vertices:
            if i != j:
                min_weight_match.add_edge(i, j, weight=G[i][j])
    mate = nx.algorithms.matching.min_weight_matching(min_weight_match, maxcardinality=True)
    return mate

def christofides_tsp(coordinates):
    num_cities = len(coordinates)
    dist_matrix = calculate_distance_matrix(coordinates)
    
    # Minimum Spanning Tree (MST)
    mst = minimum_spanning_tree(csr_matrix(dist_matrix))
    mst = mst.toarray()
    
    # Find odd degree vertices in MST
    odd_vertices = [i for i in range(num_cities) if np.sum(mst[i] > 0) % 2 != 0]
    
    # Minimum Weight Perfect Matching (MWPM) for the odd degree vertices
    subgraph = nx.complete_graph(len(odd_vertices))
    for i in range(len(odd_vertices)):
        for j in range(i+1, len(odd_vertices)):
            ii = odd_vertices[i]
            jj = odd_vertices[j]
            subgraph[i][j]['weight'] = dist_matrix[ii][jj]
    matching = minimum_weight_perfect_matching(subgraph, odd_vertices)
    
    # Build Multigraph including MST and Matching
    multi_graph = np.copy(mst)
    for edge in matching:
        i, j = edge
        ii = odd_vertices[i]
        jj = odd_vertices[j]
        multi_graph[ii][jj] += dist_matrix[ii][jj]
        multi_graph[jj][ii] += dist_matrix[jj][ii]
    
    # Eulerian tour on the MultiGraph (multi_graph)
    _, preorder = depth_first_order(csr_matrix(multi->graph), i_start=0, directed=False)
    
    # Making the tour a Hamiltonian circuit (removing repeated nodes)
    hamiltonian_tour = []
    visited = set()
    for i in preorder:
        if i not in visited:
            visited.add(i)
            hamiltonian_tour.append(i)
    hamiltonian_tour.append(hamiltonian_tour[0])  # To return to the starting point

    # Calculate total cost of the Hamiltonian circuit
    total_cost = sum(dist_matrix[hamiltonian_tour[i], hamiltonian_tour[i+1]] for i in range(len(hamiltonian_tour) - 1))
    
    return hamiltonian_tour, total_cost

coordinates = np.array([
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
])

tour, total_cost = christofides_tsp(coordinates)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")