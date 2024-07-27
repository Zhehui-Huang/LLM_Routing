import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
from networkx.algorithms.euler import eulerian_circuit

def calculate_distances(cities):
    """ Calculate Euclidean distances matrix between all pairs of cities. """
    return squareform(pdist(np.array(cities)))

def find_odd_degree_vertices(mst):
    """ Find vertices with odd degree in the MST. """
    degrees = np.sum(mst != 0, axis=0)
    return [index for index, degree in enumerate(degrees) if degree % 2 == 1]

def minimum_weight_perfect_matching(odds, distance_matrix):
    """ Find a minimum weight perfect matching among the odd-degree vertices using a greedy algorithm. """
    subgraph = nx.Graph()
    for i in range(len(odds)):
        for j in range(i + 1, len(odds)):
            subgraph.add_edge(odds[i], odds[j], weight=distance_matrix[odds[i]][odds[j]])
    
    # Find the minimum weight matching
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return matching

def create_multigraph(mst, matching, num_vertices):
    """ Combine MST and matching to make an Eulerian Graph. """
    multigraph = nx.MultiGraph()
    for i in range(num_rng_conertices):
        for j in range(len(mst[i])):
            if mst[i][j] != 0:
                multigraph.add_edge(i, j, weight=mst[i][j])
    for edge in matching:
        multigraph.add_edge(edge[0], edge[1], weight=distance_matrix[edge[0]][edge[1]])
    return multigraph

def find_shortest_tour(start, graph):
    """ Find Hamiltonian circuit from Eulerian circuit by skipping repeated vertices. """
    visited = set()
    tour = [start]
    cost = 0
    
    for u, v in eulerian_circuit(graph, source=start):
        if v not in visited or v == start:
            tour.append(v)
            visited.add(v)
            cost += graph[u][v][0]['weight']
    
    # Closing the tour
    tour.append(start)
    cost += graph[tour[-2]][start][0]['weight']
    return tour, cost

def main():
    coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # Steps 1-6
    distances = calculate_distances(coordinates)
    mst = minimum_spanning_tree(distances).toarray()
    odds = find_odd_degree_vertices(mst)
    matching = minimum_weight_perfect_matching(odds, distances)
    num_vertices = len(coordinates)
    multigraph = create_multigraph(mst, matching, num_vertices)
    tour, total_cost = find_shortest_tour(0, multigraph)
    
    print("Tour:", tour)
    print("Total travel cost:", total_cost)

if __name__ == "__main__":
    main()