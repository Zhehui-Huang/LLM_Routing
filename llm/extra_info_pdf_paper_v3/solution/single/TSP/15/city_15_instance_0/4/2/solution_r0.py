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

def minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph, weight='weight')

def odd_degree_vertices(tree):
    return [v for v, degree in dict(tree.degree()).items() if degree % 2 != 0]

def minimum_weight_matching(graph, odd_vertices):
    subgraph = graph.subgraph(odd_vertices)
    return nx.algorithms.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def combine_mst_and_matching(mst, matching):
    augmented_graph = nx.Graph(mst)
    augmented_graph.add_edges_from(matching)
    return augmented_graph

def eulerian_circuit(graph):
    return list(nx.eulerian_circuit(graph))

def make_hamiltonian_circuit(circuit, graph):
    visited = set()
    path = []
    cost = 0
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        last = v
        cost += graph.get_edge_data(u, v)['weight']
    path.append(last)
    visited.add(last)
    # Connect back to start
    if path[0] != path[-1]:
        path.append(path[0])
        cost += graph.get_edge_data(path[-1], path[0])['weight']
    return path, cost

def solve_tsp(coordinates):
    graph = construct_graph(coordinates)
    mst = minimum_spanning_tree(graph)
    odd_vertices = odd_degree_vertices(mst)
    matching = minimum_weight_matching(graph, odd_vertices)
    augmented_graph = combine_mst_and_matching(mst, matching)
    circuit = eulerian_circuit(augmented_graph)
    tour, total_cost = make_hamiltonian_circuit(circuit, graph)
    return tour, total_cost

# Solve the TSP
tour, total_cost = solve_tsp(coordinates)

# Output results in format required
print("Tour:", tour)
print("Total travel cost:", total_cost)