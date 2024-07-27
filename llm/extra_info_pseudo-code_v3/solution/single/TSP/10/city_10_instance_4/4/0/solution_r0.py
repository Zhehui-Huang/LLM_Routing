import math
from scipy.spatial.distance import cdist
import numpy as np
import networkx as nx

# Given city coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Construct the complete graph
def construct_graph(cities):
    G = nx.Graph()
    for i in cities.keys():
        for j in cities.keys():
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Christofides algorithm main function
def christofides_tsp(cities):
    G = construct https://christofides-tsp-full-solution.netlify.app/graph(cities)
    
    # Step 1: Compute a Minimum Spanning Tree (MST) using Kruskal's
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices with odd degree
    odd_vertices = [v for v, d in T.degree() if d % 2 == 1]
    
    # Step 3: Find minimum-weight perfect matching
    # Due to small input size, use networkx for simplicity
    min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_vertices), maxcardinality=True)
    
    # Step 4: Combine edges of T and M to form a multigraph
    MG = nx.MultiGraph(T)
    MG.add_edges_from(min_weight_matching)
    
    # Step 5: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(MG))
    
    # Step 6: Convert Eulerian to Hamiltonian path
    seen = set()
    hamiltonian_circuit = [0]
    for u, _ in eulerian_circuit:
        if u not in seen:
            seen.add(u)
            hamiltonian_circuit.append(u)
    hamiltonian_circuit.append(0)  # return to the depot
    
    # Calculate the total travel cost
    total_distance = sum(euclidean_distance(cities[hamiltonian_circuit[i]], cities[hamiltonian_circuit[i+1]])
                         for i in range(len(hamiltonian_circuit)-1))
    
    return hamiltonian_circuit, total_distance

# Execute the TSP algorithm
tour, cost = christofides_tsp(cities)
print("Tour:", tour)
print("Total travel cost:", cost)