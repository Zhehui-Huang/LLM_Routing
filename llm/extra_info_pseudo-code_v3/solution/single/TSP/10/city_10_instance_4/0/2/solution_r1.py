import numpy as np
from scipy.spatial.distance import cdist
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

def christofides_tsp(points):
    num_points = len(points)
    # Step 0: Prepare the graph from points
    dist_matrix = cdist(points, points)
    sparse_dist_matrix = minimum_spanning_tree(dist_matrix)
    G = nx.Graph(sparse_dist_matrix)

    # Step 1: Calculate minimum spanning tree (MST) of G
    T = nx.minimum_spanning_tree(G, weight='weight')

    # Step 2: Find vertices with odd degree in the MST T
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

    # Step 3: Find a minimum weight perfect matching M in the induced subgraph on odd vertices
    subgraph = T.subgraph(odd_degree_nodes)
    M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

    # Step 4: Create a multigraph by combining T and M
    multi_G = nx.MultiGraph(T)
    multi_G.add_edges_from(M)

    # Step 5: Find an Eulerian circuit in the multigraph
    euler_path = list(nx.eulerian_circuit(multi_G, source=0))

    # Step 6: Make the Eulerian path a Hamiltonian path (shortcutting)
    visited = set()
    hamiltonian_circuit = [0]

    for u, _ in euler_path:
        if u not in visited:
            visited.add(u)
            hamiltonian_circuit.append(u)

    hamiltonian_circuit.append(0)  # Complete the circuit by going back to the start

    # Calculate the total cost of the Hamiltonian path
    total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

    return hamiltonian_circuit, total_cost

# Define points for the cities
locations = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Calculate the tour and cost
tour, total_cost = christofides_tsp(locations)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)