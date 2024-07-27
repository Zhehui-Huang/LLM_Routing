import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations
import matplotlib.pyplot as plt

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Create a complete graph
def create_complete_graph(cities, calculate_distance):
    G = nx.Graph()
    for city1 in cities:
        for city2 in cities:
            if city1 != city2:
                G.add_edge(city1, city2, weight=calculate_distance(city1, city2))
    return G

# Main Christofides algorithm function
def christofides_algorithm(cities):
    # Step 1. Create the complete graph
    G = create_complete_graph(cities, calculate_distance)
    
    # Step 2. Minimum spanning tree T
    T = nx.minimum_spanning_tree(G, weight='weight')
    
    # Step 3. Vertices with odd degree
    odd_degree_nodes = [v for v in T.nodes if T.degree(v) % 2 != 0]
    
    # Step 4. Minimum weight perfect matching M on odd degree vertices
    odd_graph = G.subgraph(odd_degree_nodes)
    M = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)
    
    # Step 5. Combine edges of T and edges from M to form a multigraph
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(M)
    
    # Step 6. Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))
    
    # Step 7. Make it a Hamiltonian circuit by skipping visited nodes
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # complete the tour

    # Calculate path cost
    cost = 0
    for i in range(1, len(path)):
        cost += calculate_distance(path[i-1], path[i])
    
    return path, cost

# Solve the problem using the implemented algorithm
path, cost = christofides_algorithm(cities)

# Output the path and cost
print("Tour:", path)
print("Total travel cost:", cost)