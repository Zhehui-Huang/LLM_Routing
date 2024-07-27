import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean

# Define city coordinates
city_positions = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Function to create a graph with cities, including depot as node 0
def create_complete_graph(city_positions):
    G = nx.Graph()
    cities = city_positions.keys()
    for i in cities:
        for j in cities:
            if i != j:
                distance = euclidean(city_positions[i], city_positions[j])
                G.add_edge(i, j, weight=distance)
    return G

# Function to find the shortest Hamiltonian tour using Christofides algorithm
def christofides_algorithm(G):
    # Step 1: Create MST
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices with odd degree
    odd_degree_vertices = [v for v, d in T.degree() if d % 2 != 0]
    
    # Step 3: Minimum weight matching
    min_weight_matching = nx.Graph()
    min_weight_matching.add_nodes_from(odd_degree_vertices)
    for u, v in combinations(odd_degree_vertices, 2):
        min_weight_matching.add_edge(u, v, weight=G[u][v]['weight'])
    matching = nx.algorithms.matching.min_weight_matching(min_weight_matching, weight='weight')
    
    # Step 4: Combine MST and minimum-weight matching
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(matching)
    
    # Step 5: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))
    
    # Step 6: Convert to Hamiltonian path, skipping repeated nodes
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Complete the tour
    
    # Calculate the total travel cost
    total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
    
    return path, total_cost

# Create graph and calculate tour
graph = create_complete_graph(city_positions)
tour, total_cost = christofides_algorithm(graph)

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")