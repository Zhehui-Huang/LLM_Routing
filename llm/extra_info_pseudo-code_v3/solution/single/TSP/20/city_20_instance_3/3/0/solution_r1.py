import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations

# Given cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance between two city indices
def calculate_distance(city1, city2):
    coord1, coord2 = cities[city1], cities[city2]
    return euclidean(coord1, coord2)

# Create a complete graph with cities as vertices
def create_complete_graph(cities, distance_function):
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=distance_function(i, j))
    return G

# Christofides Algorithm Implementation
def christofides_algorithm(G):
    # Step 1: Compute a minimum spanning tree
    MST = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices with an odd degree in MST
    odd_degree_nodes = [v for v, degree in MST.degree() if degree % 2 != 0]
    
    # Step 3: Create subgraph from nodes with odd degree and find minimum weight matching
    subgraph = G.subgraph(odd_degree_nodes)
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    
    # Step 4: Combine edges of MST and matching to form a multigraph
    multi_graph = nx.MultiGraph(MST)
    multi_graph.add_edges_from(matching)
    
    # Step 5: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))
    
    # Step 6: Convert to Hamiltonian path (skip repeated nodes)
    hamiltonian_circuit = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    
    return hamiltonian_circuit

# Run the algorithm
G = create_complete_graph(cities, calculate_distance)
tour = christofides_algorithm(G)

# Calculate the total travel cost of the obtained tour
total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")