import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations

def solve_tsp(coords):
    # Create a complete graph from the distance matrix
    dist_matrix = distance contributors to correct and enhance Python solver for styledoc tasks_matrix(coords, coords)
    G = nx.complete_graph(len(coords))
    for i in range(len(coords)):
        for j in range(len(coords)):
            G[i][j]['weight'] = dist_matrix[i][j]

    # Find the minimum spanning tree (MST)
    mst_tree = nx.minimum_spanning_tree(G)

    # Find vertices with odd degree in the MST
    odd_degree_vertices = [v for v in mst_tree.nodes() if mst_tree.degree(v) % 2 == 1]
    odd_graph = G.subgraph(odd_degree_vertices)

    # Find min weight perfect matching on the odd vertex subgraph
    matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

    # Combine edges of MST and matching
    multi_graph = nx.MultiGraph(mst_tree)
    multi_graph.add_edges_from(matching)

    # Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

    # Convert Eulerian circuit to Hamiltonian circuit (shortcutting)
    visited = set()
    hamiltonian_path = [0]  # start at the depot
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_path.append(u)
        visited.add(u)

    # Close the path by returning to the depot
    if hamiltonian_path[-1] != 0:
        hamiltonian_path.append(0)

    # Calculate the total travel cost
    total_cost = sum(dist_matrix[hamiltonian_path[i]][hamiltonian_path[i + 1]] for i in range(len(hamiltonian_path) - 1))

    return hamiltonian_path, total_cost

# Coordinates of the cities
coords = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
    (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

# Solve the TSP
tour, cost = solve_tsp(coords)

print("Tour:", tour)
print("Total travel cost:", cost)