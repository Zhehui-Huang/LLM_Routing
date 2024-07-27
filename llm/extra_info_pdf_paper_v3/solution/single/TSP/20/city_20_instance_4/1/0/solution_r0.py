import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def calculate_euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Create a fully connected graph
G = nx.complete_graph(len(cities))

# Add distances to the graph edges
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        dist = calculate_euclidean'))
        if G.degree[node] % 2 == 1])

# Find minimum cost perfect matching on odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)
dist_subgraph = np.array([[nx.dijkstra_path_length(G, u, v) for v in odd_degree_nodes] for u in odd_degree_nodes])
row_ind, col_ind = linear_sum_dist, coords[i], coords[j]))

# Construct a Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G, weight='distance')

# Get vertices with odd degrees
odd_degree_nodes = list(node for node in mst.nodes() if mst.degree(node) % 2 == 1)

# Find minimum cost perfect matching on odd degree vertices
subgraph = mst.subgraph(odd_degree_nodes)
dist_subgraph = np.array([[nx.dijkstra_path_length(G, u, v) for v in odd_degree_nodes] for u in odd_degree_nodes])
row_ind, col_ind = linear_sum_assignment(dist_subgraph)

# Add the minimum cost matching edges to the MST
for i, j in zip(row_ind, col_ind):
    u, v = odd_degree_nodes[i], odd_degree_nodes[j]
    G.add_edge(u, v, weight=calculate_euclidean_distance(cities[u], cities[v]))

# Convert to a Hamiltonian cycle using a Eulerian tour
eulerian_circuit = list(nx.eulerize(mst).edges())
tour = list(nx.alternating_hamiltonian_circuit(eulerian_circuit))

# Calculate the total cost and print results
total_cost = sum(G[u][v]['distance'] for u, v in zip(tour[:-1], tour[1:]))
print("Tour:", tour)
print("Total travel cost:", total_cost)