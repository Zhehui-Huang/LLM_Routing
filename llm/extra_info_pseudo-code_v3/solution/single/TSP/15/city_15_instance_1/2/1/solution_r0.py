import numpy as np
import networkx as nx
from scipy.spatial import distance
from itertools import combinations

# Defining cities' coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Step 1: Compute a minimum spanning tree (MST) T of G.
def compute_euclidean_distance_matrix(cities):
    """ Computes the Euclidean distance matrix. """
    keys = sorted(cities.keys())
    points = [cities[key] for key in keys]
    return distance.cdist(points, points, 'euclidean'), keys

def find_minimum_spanning_tree(distance_matrix, keys):
    """ Computes the minimum spanning tree using NetworkX. """
    G = nx.Graph()
    for i, key_i in enumerate(keys):
        for j, key_j in enumerate(keys):
            if i != j:
                G.add_edge(key_i, key_j, weight=distance_matrix[i][j])

    T = nx.minimum_spanning_tree(G)
    return T

distance_matrix, keys = compute_euclidean_distance_matrix(cities)
T = find_minimum_spanning_tree(distance_matrix, keys)

# Step 2: Identify the set O of vertices with odd degree in T.
def find_odd_degree_vertices(T):
    """ Finds vertices with an odd degree in the graph. """
    return [v for v, d in T.degree() if d % 2 == 1]

O = find_odd_degree_vertices(T)

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O.
def find_minimum_weight_matching(T, O):
    """ Finds a minimum weight perfect matching in the given subgraph of odd degree vertices. """
    subgraph = T.subgraph(O).copy()
    matching = nx.algorithms.max_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return matching

M = find_minimum_weight_matching(T, O)

# Step 4: Combine edges of T and M to create a multigraph H
def create_multigraph(T, M):
    """ Combines edges of T and M to create a multigraph. """
    H = T.copy()
    H.add_edges_from(M)
    return H

H = create_multigraph(T, M)

# Step 5: Find an Eulerian circuit in H.
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices.
def create_hamiltonian_circuit(eulerian_circuit):
    """ Converts an Eulerian circuit to a Hamiltonian circuit by skipping visited nodes. """
    seen = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in seen:
            hamiltonian_circuit.append(u)
            seen.add(u)
    hamiltonian_circuit.append(0)  # Complete the tour
    return hamiltonian_circuit

hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)

# Calculate total travel cost
def calculate_total_cost(circuit, distance_matrix, keys):
    total_cost = 0
    for i in range(len(circuit) - 1):
        idx1, idx2 = keys.index(circuit[i]), keys.index(circuit[i+1])
        total_cost += distance_matrix[idx1][idx2]
    return total_cost

total_cost = calculate_total_cost(hamiltonian_circuit, distance_matrix, keys)

# Outputting the final results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)