import math
import networkx as nx
from itertools import combinations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def christofides(cities):
    # Number of cities and complete graph
    n = len(cities)
    G = nx.complete_graph(n)
    
    # Set the edge attributes
    for i in range(n):
        for j in range(i+1, n):
            G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

    # Step 1: Compute Minimum Spanning Tree
    T = nx.minimum_spanning_tree(G)

    # Step 2: Find set O of vertices with odd degree
    odd_vertices = [v for v in T.nodes() if T.degree(v) % 2 == 1]

    # Step 3: Find minimum weight perfect matching M in the induced subgraph created by O
    min_weight_subgraph = G.subgraph(odd_vertices)
    M = nx.Graph()
    M.add_nodes_from(min_weight_subgraph.nodes(data=True))
    min_weight_matching = nx.algorithms.matching.min_weight_matching(min_weight_subgraph, maxcardinality=True, weight='weight')
    
    M.add_edges_from(min_weight_matching)

    # Step 4: Combine edges of T and M to form a multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(M.edges(data=True))

    # Step 5: Find Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(H))

    # Step 6: Convert Eulerian circuit to Hamiltonian path
    visited = set()
    hamiltonian_circuit = []
    for u, _ in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_circuit.append(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0]) # return to depot

    # Calculate total travel cost
    total_cost = 0
    for i in range(len(hamiltonian_circuit)-1):
        total_cost += G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight']
    
    return hamiltonian_circuit, int(total_cost)

# Define city coordinates
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Find the tour and cost
tour, cost = christofides(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", cost)