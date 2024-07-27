import numpy as np
from scipy.spatial.distance import cdist
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from networkx import Graph, eulerian_circuit
from networkx.algorithms.matching import min_weight_matching

def christofides_tsp(points):
    num_points = len(points)

    # Compute the Euclidean distance matrix
    dist_matrix = cdist(points, points)

    # Step 1: Compute a minimum spanning tree (MST)
    mst_tree = minimum_spanning_tree(dist_matrix).toarray()

    # Step 2: Identify vertices with odd degree in the MST
    degree = np.sum(mst_tree > 0, axis=0)
    odd_degree_vertices = np.where(degree % 2 == 1)[0]

    # Step 3: Find a minimum-weight perfect matching among the odd degree vertices
    subgraph = Graph()
    subgraph.add_weighted_edges_from(
        (i, j, dist_matrix[i][j]) for i in odd_degree_vertices for j in odd.degree_vertices if i < j
    )
    matching = min_weight_matching(subgraph, maxcardinality=True, weight='weight')

    # Step 4: Combine the edges of MST and the matching to form a multigraph
    mst_graph = Graph()
    mst_graph.add_weighted_edges_from(
        (i, j, dist_matrix[i][j]) for i in range(num_points) for j in range(i+1, num_points) if mst_tree[i][j] > 0
    )
    mst_graph.add_edges_from(matching)
    
    # Step 5: Find an Eulerian circuit in the multigraph
    eulerian_path = list(eulerian_circuit(mst_graph, source=0))
    eulerian_path = [edge[0] for edge in eulerian_path]
    eulerian_path.append(0)  # complete the circuit by returning to the start

    # Step 6: Convert the Eulerian circuit to a Hamiltonian circuit without repeating vertices
    visited = set()
    hamiltonian_circuit = []
    for vertex in eulerian_path:
        if vertex not in visited:
            visited.add(vertex)
            hamiltonian_circuit.append(vertex)

    hamiltonian_circuit.append(0)  # complete the circuit by returning to the start

    # Get tour cost
    cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

    return hamiltonian_circuit, cost

# Points
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

tour, total_cost = christofides_tsp(locations)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)