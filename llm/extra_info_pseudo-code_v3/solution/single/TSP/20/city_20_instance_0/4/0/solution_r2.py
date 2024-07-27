import math
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Calculate distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with weights as distances
def create_complete_graph():
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Find minimum weight perfect matching from odd vertex subset
def minimum_weight_perfect_matching(G, odd_vertices):
    min_weight_matching = nx.Graph()
    while odd_vertices:
        v = odd_vertices.pop()
        distances = [(G[v][u]['weight'], u) for u in odd_vertices]
        min_distance, u = min(distances)
        odd_vertices.remove(u)
        min_weight_matching.add_edge(v, u, weight=min_distance)
    return min_weight_matching

# Christofides Algorithm Implementation
def christofides_algorithm():
    G = create_complete_graph()
    # 1. Compute a minimum spanning tree (MST) T of G.
    T = nx.minimum_spanning_tree(G)
    # 2. Identify the set O of vertices with odd degree in T.
    odd_vertices = [node for node in T.nodes() if T.degree(node) % 2 == 1]
    # 3. Find a minimum-weight perfect matching M in the subgraph induced by O.
    M = minimum_weight_perfect_matching(G, odd_vertices)
    # 4. Combine the edges of T and M to form a multigraph H where each vertex has even degree.
    H = nx.MultiGraph(T)
    H.add_edges_from(M.edges(data=True))
    # 5. Find an Eulerian circuit in H.
    eulerian_circuit = list(nx.eulerian_circuit(H, source=0))
    # 6. Convert the Eulerian circuit into a Hamiltonian circuit
    visited = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0])  # to return to the initial node
    
    # Calculate the total travel cost
    total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

    return hamiltonasian_circuit, total_cost

# Execute the function and print the results
tour, total_cost = christofides_algorithm()
print("Tour:", tour)
print("Total travel cost:", total_cost)