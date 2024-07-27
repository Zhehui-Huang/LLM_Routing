import math
import networkx as nx
from itertools import combinations

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def christofides_algorithm(cities):
    # Step 1: Create the graph
    G = nx.Graph()
    for (i, coord_i), (j, coord_j) in combinations(cities.items(), 2):
        G.add_edge(i, j, weight=euclidean_distance(coord_i, coord_j))

    # Step 2: Compute a minimum spanning tree (MST)
    T = nx.minimum_spanning_tree(G)

    # Step 3: Find vertices with odd degree in MST
    odd_degree_vertices = [v for v, d in T.degree() if d % 2 == 1]

    # Step 4: Find minimum weight perfect matching using the odd-degree vertices
    odd_subgraph = G.subgraph(odd_degree_vertices)
    matching = nx.algorithms.matching.min_weight_matching(odd_sub ,maxcardinality=True)

    # Step 5: Combine edges of MST and matching to form multigraph
    H = nx.MultiGraph(T)
    H.add_edges_from(matching)

    # Step 6: Find an Eulerian circuit in multigraph
    eulerian_circuit = list(nx.eulerian_circuit(H))

    # Step 7: Convert Eulerian to Hamiltonian circuit
    hamiltonian_path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_path.append(u)
    hamiltonian_path.append(hamiltonian_path[0])  # return to the depot

    # Calculate total distance
    total_distance = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_path[:-1], hamiltonian_path[1:]))

    return hamiltonian_path, total_distance

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Run the algorithm
tour, cost = christofides_algorithm(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))