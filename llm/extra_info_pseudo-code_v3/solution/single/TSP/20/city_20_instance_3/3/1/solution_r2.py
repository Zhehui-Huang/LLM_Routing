import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

def calculate_distances(coordinates):
    """ Calculate Euclidean distances matrix for all city pairs. """
    return squareform(pdist(coordinates))

def find_odd_degree_nodes(tree):
    """ Find nodes of the minimum spanning tree with odd degree. """
    degree_sequence = np.sum(tree != 0, axis=0)
    return [index for index, degree in enumerate(degree_sequence) if degree % 2 == 1]

def perfect_matching(odd_nodes, distance_matrix):
    """ Compute a minimum weight perfect matching for the odd-degree nodes."""
    graph = nx.Graph()
    for node in odd_nodes:
        for other in odd_nodes:
            if node != other:
                graph.add_edge(node, other, weight=distance_matrix[node, other])

    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True, weight='weight')
    return matching

def combine_multigraph(mst, matching):
    """ Combine the edges of the MST and the perfect matching. """
    graph = nx.from_numpy_matrix(mst, create_using=nx.MultiGraph)
    for u, v in matching:
        graph.add_edge(u, v)
    return graph

def find_eulerian_circuit(graph):
    """ Find Eulerian circuit in the graph. """
    return list(nx.eulerian_circuit(graph))

def shortcut_eulerian_circuit(circuit):
    """ Shortcut the Eulerian circuit to form a Hamiltonian circuit. """
    path = []
    visited = set()
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    if path[-1] != path[0]:
        path.append(path[0])  # Ensure it is a circuit by coming back to the start
    return path

def calculate_total_distance(path, distance_matrix):
    """ Calculate the total distance of the tour. """
    total_distance = sum(distance_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))
    return total_distance

def main():
    # Coordinates of the cities including the depot
    coordinates = np.array([
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ])

    distances = calculate_distances(coordinates)
    mst_matrix = minimum_spanning_tree(distances).toarray()
    odd_nodes = find_odd_degree_nodes(mst_matrix)
    matching = perfect_matching(odd_nodes, distances)
    multi_graph = combine_multigraph(mst_matrix, matching)
    eulerian = find_eulerian_circuit(multi_graph)
    hamiltonian_path = shortcut_eulerian_circuit(eulerian)
    total_distance = calculate_total_distance(hamiltonian_path, distances)

    print("Tour:", hamiltonian_path)
    print("Total travel cost:", total_distance)

if __name__ == "__main__":
    main()