import networkx as nx
import numpy as np
from itertools import combinations

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def create_complete_graph(node_coords):
    G = nx.Graph()
    n = len(node_coords)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(node_coords[i], node_coords[j]))
    return G

def minimum_weight_perfect_matching(G, odd_degree_nodes):
    subgraph = G.subgraph(odd_degree_nodes).copy()
    mwpm = nx.Graph()
    pairs = min_weight_matching(subgraph)
    for u, v in pairs:
        mwpm.add_edge(u, v, weight=G[u][v]['weight'])
    return mwpm

def min_weight_matching(G):
    import networkx.algorithms.matching as matching
    mates = matching.min_weight_matching(G, maxcardinality=True)
    return mates

def find_eulerian_circuit(G, starting_node=0):
    return list(nx.eulerian_circuit(G, source=starting_node))

def christofides_algorithm(cities):
    n = len(cities)
    
    # Step 1: Create the complete graph
    G = create_complete_graph(cities)
    
    # Step 2: Compute MST
    T = nx.minimum_spanning_tree(G)
    
    # Step 3: Find odd degree vertices
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 != 0]
    
    # Step 4: Find minimum weight perfect matching M in the subgraph induced by odd_degree_nodes
    M = minimum_weight_perfect_matching(G, odd_degree_nodes)
    
    # Step 5: Combine the edges of T and M to form a multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(M.edges(data=True))
    
    # Step 6: Find an Eulerian circuit
    eulerian_circuit = find_eulerian_circuit(H)
    
    # Step 7: Convert the Eulerian circuit to a Hamiltonian circuit
    visited = set()
    path = [0]
    for u, v in eulerian_circuit:
        if v not in visited or v == 0:
            path.append(v)
            visited.add(v)
    
    # Calculate the total travel cost
    total_cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
    
    return path, total_cost

# Define the coordinates per the given data
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Compute the tour and total cost
tour, total_cost = christofides_algorithm(cities)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)