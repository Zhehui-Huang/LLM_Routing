import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Define the coordinates of each city
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Compute the distance matrix
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Create a graph based on the distance matrix
G = nx.Graph()
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        G.add_edge(i, j, weight=dist_input[i][j])

# Find the minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Get all nodes in the MST with odd degree to perform perfect matching
odd_degree_nodes = [n for n in mst.nodes if mst.degree(n) % 2 == 1]
subgraph = mst.subgraph(odd_degree_nodes)

# Compute minimum-cost perfect matching on the subgraph of odd degree nodes
odds = list(subgraph.nodes)
edge_weights = np.array([[dist_input[i][j] for j in odds] for i in odds])
row_ind, col_ind = linear_sum_assignment(edge_weights)
min_matching = [(odds[row_ind[i]], odds[col, ind[i]]) for i in range(len(row_ind))]

# Add the edges from the minimum-cost perfect matching to the MST
for i, j in min_matching:
    mst.add_edge(i, j, weight=dist_input[i][j])

# Create an Eulerian circuit from the MST
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit (shortcutting)
visited = set()
tour = []
cost = 0.0
last = 0
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        tour.append(u)
        cost += dist_input[last][u]
        last = u
tour.append(0)
cost += dist_input[last][0]  # returning to the start

# Output the results
print("Tour:", tour)
print("Total travel cost:", cost)