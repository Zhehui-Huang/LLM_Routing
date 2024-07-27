import math
import networkx as nx
from itertools import combinations

# Define cities' coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Create a complete graph with weighted edges (euclidean distance)
def create_complete_graph(city_coordinates):
    G = nx.Graph()
    for city1, coord1 in city_coordinates.items():
        for city2, coord2 in city_coordinates.items():
            if city1 != city2:
                G.add_edge(city1, city2, weight=euclidean_distance(coord1, coord2))
    return G

# Christofides algorithm implementation
def christofides_algorithm(G):
    # Step 1: Compute the MST of the graph
    T = nx.minimum_spanning_tree(G, weight='weight')
    
    # Step 2: Identify vertices with an odd degree
    odd_vertices = [v for v, degree in T.degree() if degree % 2 == 1]
    
    # Step 3: Find a minimum weight perfect matching
    odd_vertex_subgraph = G.subgraph(odds_vertices)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_vertex_subgraph, maxcardinality=True, weight='weight')
    
    # Step 4: Combine the edges of T and M
    T.add_edges_from(min_weight_matching)
    
    # Step 5: Find Eulerian circuit
    euler_circuit = list(nx.eulerian_circuit(T, source=0))
    
    # Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
    seen = set()
    path = []
    for u, v in euler_circuit:
        if u not in seen:
            path.append(u)
            seen.add(u)
    path.append(0)  # Append the start point to make it a cycle
    
    # Calculate the total weight of the Hamiltonian path
    total_cost = sum(G[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
    
    return path, total_cost

# Create the complete graph
graph = create_complete_graph(cities)

# Solve the TSP problem
tour, total_travel_cost = christofides_algorithm(graph)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)