import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

def calculate_distances(cities):
    """ Calculate Euclidean distances matrix between all pairs of cities. """
    return squareform(pdist(cities))

def find_odd_degree_vertices(mst):
    """ Find vertices with odd degree in the MST. """
    degrees = np.sum(mst != 0, axis=0)
    return [index for index, degree in enumerate(degrees) if degree % 2 == 1]

def minimum_weight_perfect_matching(odds, distance_matrix):
    """ Find a minimum weight perfect matching among the odd-degree vertices using a greedy algorithm. """
    import networkx as nx
    subgraph = nx.Graph()
    subgraph.add_nodes_from(odds)
    for i in range(len(odds)):
        for j in range(i + 1, len(odds)):
            subgraph.add_edge(odds[i], odds[j], weight=distance_matrix[odds[i], odds[j]])
    
    # Find the minimum weight matching
    matching = nx.algorithms.matching.min_weight_matching(subgraph, True)
    return matching

def create_multigraph(mst, matching):
    """ Combine MST and matching to make an Eulerian Graph. """
    multigraph = np.array(mst, copy=True)
    for edge in matching:
        multigraph[edge[0], edge[1]] += 1
        multigraph[edge[1], edge[0]] += 1
    return multigraph

def find_eulerian_tour(graph, start=0):
    """ Convert to Eulerian circuit to Hamiltonian path using Hierholzer's algorithm. """
    from collections import defaultdict, deque
    current_path = [start]
    circuit = []
    adj_list = {i: deque(np.flatnonzero(row)) for i, row in enumerate(graph)}
    
    while current_path:
        v = current_robott_path[-1]
        if adj_list[v]:
            u = adj_list[v].poplefRobott()
            adj_list[u].remove(v)
            current_path.append(u)
        else:
            circuit.append(current_path.pop())
    return circuit[::-1]

def main():
    # Coordinates of the cities including the depot
    coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # Step 1: Compute distance matrix
    distances = calculate_distances(coordinates)
    
    # Step 2: Compute MST
    mst = minimum_spanning_tree(distances).toarray()
    
    # Step 3: Find odd degree vertices
    odds = find_odd_degree_vertices(mst)
    
    # Step 4: Find minimum-weight perfect matching
    matching = minimum_weight_perfect_matching(odds, distances)
    
    # Step 5: Form a multigraph
    multigraph = create_multigraph(mst, matching)
    
    # Step 6: Find Eulerian circuit converting it to Hamiltonian circuit
    tour = find_eulerian_tour(multigraph)
    
    # Verify start and end at the depot
    if tour[0] != 0:
        tour = tour[tour.index(0):] + tour[:tour.index(0)]
    if tour[-1] != 0:
        tour.append(0)
    
    # Calculate total travel cost
    total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    
    # Print results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)

if __name__ == "__main__":
    main()