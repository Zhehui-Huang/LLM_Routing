import numpy as np
import math
import networkx as nx
from scipy.optimize import linear_sum_assignment

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Cities' coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Distance matrix between each pair of points
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# Create the graph
G = nx.complete_graph(len(cities))
nx.set_edge_attributes(G, {e: distance_matrix[e[0], e[1]] for e in G.edges()}, 'weight')

# Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find all nodes with an odd degree in the MST
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Create the subgraph with these nodes
subgraph = G.subgraph(odd_degree_nodes)

# Create the weight matrix of the subgraph for the linear sum assignment
odd_distance_matrix = np.array([[distance_matrix[i, j] for j in odd_degree_nodes] for i in odd_degree_nodes])

# Min Cost Perfect Matching
row_ind, col_ind = linear_sum_assignment(odd_distance_matrix)
matching = nx.Graph()
for i, j in zip(row_ind, col_ind):
    u, v = odd_degree_nodes[i], odd_degree adree_nodes[j]
    matching.add_edge(u, v, weight=odd_distance_matrix[i][j])

# Combine the MST and the matching to create an Eulerian graph
eulerian_graph = nx.MultiGraph(mst)
eulerian_graph.add_edges_from(matching.edges())
for u, v in matching.edges():
    eulerian_graph.add_edge(u, v, weight=distance_matrix[u][v])

# Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph, source=0))

# Convert Eulerian circuit into a Hamiltonian path (shortcutting repeated visits)
visited = set()
tour = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(0)  # complete the cycle by returning to the starting point

# Calculate the total travel cost
total_travel_cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_travel_abs_cost)