import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms import tree, matching
import itertools

def calculate_euclidean_distance(points):
    return distance_matrix(points, points)

def construct_graph(num_cities, distances):
    G = nx.Graph()
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=distances[i][j])
    return G

def christofides_algorithm(cities):
    num_cities = len(cities)
    distances = calculate_euclidean_distance(cities)
    G = construct_graph(num_cities, distances)
    
    # Step 1: Compute a minimum spanning tree (MST) of G.
    T = tree.minimum_spanning_tree(G, weight='weight')
    
    # Step 2: Find vertices with an odd degree in the MST.
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 != 0]
    
    # Step 3: Find a minimum-weight perfect matching in the subgraph induced by odd-degree vertices.
    subgraph = G.subgraph(odd_degree_nodes)
    M = matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    
    # Step 4: Combine the edges of T and M to form a multigraph H.
    H = nx.MultiGraph(T)
    H.add_edges_from(M)
    
    # Step 5: Find an Eulerian circuit in H.
    eulerian_circuit = list(nx.eulerian_circuit(H))
    
    # Step 6: Convert Eulerian circuit to Hamiltonian circuit by skipping repeated vertices.
    visited = set()
    hamiltonian_circuit = [eulerian_circuit[0][0]]
    visited.add(eulerian_circuit[0][0])
    
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            hamiltonian_circuit.append(v)

    hamiltonian_circuit.append(hamiltonian_circuit[0]) # return to the starting point
    
    # Calculate the cost of the Hamiltonian circuit
    cost = sum(distances[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))
    
    return hamiltonian_circuit, cost

# Coordinates of the cities
cities = np.array([
    (50, 42), # Depot
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
])

tour, tour_cost = christofides_algorithm(cities)

# Outputting the results
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")