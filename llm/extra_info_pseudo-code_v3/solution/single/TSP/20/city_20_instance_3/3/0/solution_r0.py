import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from itertools import combinations

# Define the cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Create a complete graph with cities as nodes and distances as weights
def create_complete_graph(cities, distance_function):
    G = nx.Graph()
    G.add_nodes_from(cities)
    for (i, j) in combinations(cities, 2):
        G.add_edge(i, j, weight=distance_function(i, j))
    return G

# Implement Christofides Algorithm
def christofides_algorithm(G):
    # Step 1: Minimum Spanning Tree
    MST = nx.minimum_spanning_tree(G, weight='weight')
    
    # Step 2: Get vertices with odd degree
    odd_degree_nodes = [v for v, degree in MST.degree() if degree % 2 == 1]
    
    # Step 3: Minimum Weight Perfect Matching
    odd_subgraph = G.subgraph(odd_degree_nodes)
    matching = nx.algorithms.matching.min_weight_matching(odd_subgraph)
    
    # Step 4: Combine MST and matching
    multi_graph = nx.Graph(MST)
    multi_graph.add_edges_from(matching)
    
    # Step 5: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph))
    
    # Step 6: Create a Hamiltonian circuit
    hamiltonian_path = []
    visited = set()
    for u, v in eulerian_circuit:
        if not u in visited:
            hamiltonian_path.append(u)
            visited.add(u)
    hamiltonian_path.append(hamiltonian_path[0])  # complete the tour by going back to the depot
    return hamiltonian_path

# Main Execution
G = create_complete_graph(cities, calculate_distance)
tour = christofides_algorithm(G)

# Calculate the total cost of the tour
total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)