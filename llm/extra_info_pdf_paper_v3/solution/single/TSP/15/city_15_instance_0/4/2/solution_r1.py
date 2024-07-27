import numpy as np
import networkx as nx

# Provided coordinates for the depot and cities
coordinates = np.array([
    (9, 93),   # City 0 - Depot
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
])

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def construct_graph(coords):
    n = len(coords)
    graph = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(coords[i], coords[j])
            graph.add_edge(i, j, weight=distance)
    return graph

def solve_tsp(coordinates):
    graph = construct_graph(coordinates)
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 != 0]
    min_weight_matching = nx.algorithms.min_weight_matching(graph.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')
    mst.add_edges_from(min_weight_matching)
    euler_circuit = list(nx.eulerian_circuit(mst, source=0))
    
    # Create Hamiltonian circuit
    visited = set()
    path = [0]
    total_cost = 0
    last_node = 0

    for u, v in euler_circuit:
        if v not in visited:
            visited.add(v)
            total_cost += graph[u][v]['weight']
            path.append(v)
            last_node = v

    # Connect back to the depot
    total_cost += graph[last_node][0]['weight']
    path.append(0)

    return path, total_cost

# Solve and print the TSP solution
tour, total_cost = solve_tsp(coordinates)
print("Tour:", tour)
print("Total travel cost:", total_cost)