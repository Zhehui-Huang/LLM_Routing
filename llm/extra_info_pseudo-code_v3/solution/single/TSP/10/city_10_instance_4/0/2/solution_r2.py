import numpy as
import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from math import sqrt
from scipy.spatial.distance import pdist, squareform

def calculate_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_complete_graph(point_list, metric=calculate_distance):
    g = nx.Graph()
    num_points = len(point_list)
    for i in range(num_points):
        g.add_node(i, pos=point_list[i])

    for (i, j) in combinations(range(num_points), 2):
        g.add_edge(i, j, weight=metric(point_list[i], point_list[j]))
    return g

def min_weight_matching(G, odd_set):
    assert nx.is_weighted(G), "Graph should be weighted!"
    min_wt_match = nx.Graph()
    min_wt_match.add_nodes_from(odd_set)
    
    # Formulate as a complete graph and utilize networkx min_weight_matching
    odd_graph = nx.Graph()
    for u, v in combinations(odd_set, 2):
        wt = G[u][v]['weight']
        odd_graph.add_edge(u, v, weight=wt)
    
    min_pairs = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)
    min_wt_match.add_edges_from(min_pairs)
    return min_wt_match

def christofides(points):
    # Create complete graph
    G = create_complete_graph(points)
    
    # Step 1: Create a minimum spanning tree of G
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices of odd degree in the MST
    odd_degree_vertices = [v for v, d in T.degree() if d % 2 == 1]
    
    # Step 3: Find a minimum weight perfect matching for the odd degree vertices
    M = min_weight_matching(G, odd_degree_vertices)
    
    # Step 4: Combine the edges of T and M to form a multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(M.edges())
    
    # Step 5: Find an Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(H, source=0))
    
    # Step 6: Make it a Hamiltonian circuit by removing duplicate nodes
    visited, hamiltonian_circuit = set(), [0]
    for u, v in eulerian_circuit:
        if v not in visited or v == 0:
            visited.add(v)
            hamiltonian_circuit.append(v)

    # Calculate cost
    total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1))
    
    return hamiltonian_circuit, total_cost

# City locations
locations = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

tour, total_cost = christofides(locations)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)