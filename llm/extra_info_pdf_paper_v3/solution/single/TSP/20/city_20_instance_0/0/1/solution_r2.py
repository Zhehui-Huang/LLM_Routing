import numpy as np
import networkx as nx

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_tsp_tour():
    # Define the cities and their coordinates
    cities = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
        5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
        10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25),
        14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 
        18: (60, 63), 19: (93, 15)
    }

    # Create a complete graph
    G = nx.complete_graph(len(cities))
    for u in G.nodes:
        for v in G.nodes:
            if u != v:
                G[u][v]['weight'] = euclidean_distance(cities[u], cities[v])

    # Calculate the Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(G)

    # Find vertices with an odd degree to perform perfect matching
    odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

    # Create graph induced by vertices with odd degree
    subgraph = G.subgraph(odd_degree_nodes)
    min_cost_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

    # Add edges from Min Cost Matching to the MST
    mst_plus_matching = nx.Graph(mst)
    mst_plus_matching.add_edges_from(min_cost_matching)

    # Convert to Eulerian circuit
    eulerian_circuit_raw = list(nx.eulerian_circuit(mst_plus_matching, source=0))

    # Convert Eulerian circuit to Hamiltonian circuit by skipping visited nodes
    visited = set()
    hamiltonian_circuit = [0]
    total_distance = 0
    last_visited = 0
    for u, v in eulerian_circuit_raw:
        if v not in visited:
            visited.add(v)
            hamiltonian_circuit.append(v)
            total_distance += euclidean_distance(cities[last_visited], cities[v])
            last_visited = v

    # Return to depot
    hamiltonian_circuit.append(0)
    total_distance += euclidean_distance(cities[last_visited], cities[0])

    # Output results
    print("Tour:", hamiltonian_circuit)
    print("Total travel cost:", total_distance)

find_tsp_tour()