import math
import networkx as nx
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def christofides_algorithm(cities):
    n = len(cities)
    G = nx.Graph()
    
    # Adding vertices and weighted edges based on euclidean distances
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    
    # Step 1: Minimum spanning tree (MST)
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Vertices with odd degree in T
    O = [v for v, d in T.degree() if d % 2 == 1]
    
    # Step 3: Minimum-weight perfect matching in the subgraph induced by O
    subgraph = G.subgraph(O)
    M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    
    # Step 4: Combine the edges of T and M to form a multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(M)
    
    # Step 5: Find an Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(H))
    
    # Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
    hamiltonian_circuit = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0])  # complete the tour by returning to the start
    
    # Calculating the total travel cost
    total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1))
    
    return hamiltonian_circuit, total_cost

cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 19),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

tour, total_cost = christofides_algorithm(cities)
print("Tour:", tour)
print("Total travel cost:", "{:.2f}".format(total_cost))