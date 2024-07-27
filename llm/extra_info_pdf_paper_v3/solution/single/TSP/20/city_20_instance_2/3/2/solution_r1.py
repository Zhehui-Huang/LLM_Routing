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
        cost += dist_matrix[path[i - 1]][path[i]]
    return cost

# Christofides algorithm for TSP
def christofides(dist_matrix):
    num_cities = len(dist_matrix)
    G = nx.complete_graph(num_cities)

    # Set the weights of each edge in the graph
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G[i][j]['weight'] = dist_matrix[i][j]

    # Compute the minimum spanning tree
    MST = nx.minimum_spanning_tree(G, weight='weight')
    odd_degree_vertices = [v for v, d in MST.degree if d % 2 == 1]
    
    # Subgraph containing vertices of odd degree and find minimum weight perfect matching
    subgraph = G.subgraph(odd_degree_vertices)
    matching = nx.algorithms.max_weight_matching(subgraph, maxcardinality=True, weight="weight")

    # Add the edges from the matching to the MST
    MST.add_edges_from(matching)
    
    # Form an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

    # Convert Eulerian circuit to Hamiltonian circuit (remove repeated nodes)
    path = []
    visited = set()
    for v, _ in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            path.append(v)

    # Adding the start node at the end to complete the circuit
    path.append(path[0])

    cost = calculate_cost(path, dist_matrix)
    return path, cost

# Calculate the distance matrix
dist_matrix = calc_distance_matrix(city_coords)

# Calculate the shortest tour using Christofides algorithm
tour, total_cost = christofides(dist_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")