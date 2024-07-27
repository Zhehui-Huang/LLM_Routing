import math
import networkx as nx
import itertools

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_complete_graph(city_coords):
    G = nx.Graph()
    cities = list(city_coords.keys())
    for city1, city2 in itertools.combinations(cities, 2):
        dist = euclidean_distane(city_coords[city1], city_coords[city2])
        G.add_edge(city1, city2, weight=dist)
    return G

def find_minimum_weight_matching(G, vertices):
    subgraph = G.subgraph(vertices)
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    return matching

def christofides_algorithm(G):
    mst = nx.minimum_spanning_tree(G, weight='weight')  # Step 1
    odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 == 1]  # Step 2
    
    matching = find_minimum_weight_matching(G, odd_degree_nodes)  # Step 3
    mst.add_edges_from(matching)  # Step 4
    
    euler_circuit = list(nx.eulerian_circuit(mst, source=0))  # Step 5
    path = []
    visited = set()
    for u, _ in euler_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(0)  # To complete the circuit
    
    total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))  # Calculate path cost
    return path, total_cost

# City coordinates data
city_coords = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Create graph and execute the algorithm
G = create_complete_graph(city_coords)
tour, total_travel_cost = christofides_algorithm(G)

# Outputting the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)