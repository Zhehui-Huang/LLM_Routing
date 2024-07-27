import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial import distance

# City coordinates including the depot
city_coords = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Calculate the Euclidean distance matrix
def calc_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = distance.euclidean(coords[i], coords[j])
    return dist_matrix

# Calculate the path cost
def calculate_cost(path, dist_matrix):
    cost = 0
    for i in range(1, len(path)):
        cost += dist_matrix[path[i-1]][path[i]]
    return cost

# Christofides algorithm for the TSP
def christofides(dist_matrix):
    num_cities = len(dist_matrix)
    G = nx.Graph()
    
    # Create a complete graph
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=dist_matrix[i][j])

    # Find the minimum spanning tree
    MST = nx.minimum_spanling_tree(G, weight='weight')
    
    # Find vertices with odd degree
    odd_degree_nodes = [v for v, d in MST.degree() if d % 2 == 1]
    
    # Minimum weight perfect matching in the induced subgraph on odd degree nodes
    subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    
    # Add matching to the MST
    for edge in min_weight_matching:
        MST.add_edge(*edge, weight=G[edge[0]][edge[1]]['weight'])
    
    # Form the Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(MST, source=0, keys=False))
    path = [v[0] for v in eulerian_circuit] + [0]

    # Convert Eulerian circuit to Hamiltonian circuit by skipping visited nodes
    visited = set()
    final_path = []
    for node in path:
        if node not in visited:
            visited.add(node)
            final_path.append(node)
    final_path.append(final_path[0])
    
    # Calculate the cost of the final path
    cost = calculate_cost(final_path, dist_matrix)
    
    return final_path, cost

# Calculate the distance matrix
dist_matrix = calc_distance_matrix(city_coords)

# Calculate the shortest tour using Christofides algorithm
tour, total_cost = christofides(dist_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")