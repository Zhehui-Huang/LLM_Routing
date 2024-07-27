import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations

# Define city positions
positions = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Compute the Euclidean distance between two points
def compute_distance(pos1, pos2):
    return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Creating a complete graph
def create_graph(positions):
    G = nx.Graph()
    for i in positions:
        for j in positions:
            if i != j:
                G.add_edge(i, j, weight=compute_distance(positions[i], positions[j]))
    return G

# Christofides algorithm to find the approximate shortest path
def christofides(graph):
    # Step 1: Minimum Spanning Tree (MST)
    mst_tree = nx.minimum_spanning_tree(graph, weight='weight')
    
    # Step 2: Find vertices of odd degree
    odd_degree_nodes = [v for v, d in mst_tree.degree() if d % 2 != 0]
    
    # Step 3: Minimum weight perfect matching
    minimal_matching = nx.Graph()
    minimal_matching.add_nodes_from(odd_degree_nodes)
    for u, v in combinations(odd_degree_nodes, 2):
        minimal_matching.add_edge(u, v, weight=graph[u][v]['weight'])
    min_weight_match = nx.algorithms.matching.min_weight_matching(minimal_matching, weight='weight', maxcardinality=True)
    
    # Add minimum matching to the MST
    mst_tree.add_edges_from(min_weight_match)
    
    # Step 4: Create an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(mst_tree, source=0))
    
    # Step 5: Make the Eulerian circuit into a Hamiltonian circuit
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    if path[-1] != path[0]:
        path.append(path[0])
    
    # Calculate the path's total weight
    total_distance = sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))

    return path, total_distance

# Main execution
G = create_graph(positions)
tour, total_cost = christofides(G)

# Print the outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")