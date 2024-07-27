import math
import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
from networkx.algorithms.matching import max_weight_matching

# Define the coordinates of each city, including the depot
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def calculate_distance(coor1, coor2):
    return math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2)

# Create distance matrix
n = len(coordinates)
dist_matrix = np.array([[calculate                                                                                                                                                                                 _distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)])

# Step 1: Compute a minimum spanning tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()

# Create graph from MST
G = nx.Graph()
for i in range(n):
    for j in range(n):
        if mst[i][j] > 0:
            G.add_edge(i, j, weight=mst[i][j])

# Step 2: Find vertices with odd degree
O = [v for v in G.nodes() if G.degree(v) % 2 == 1]

# Step 3: Minimum-weight perfect matching on the subgraph induced by O
subgraph = G.subgraph(O).copy()
min_weight_match = nx.algorithms.matching.min_weight_matching(subgraph, max_weight=True)
# Add these edges to the graph
G.add_edges_from(min_weight_match)

# Step 5: Find an Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(G, source=0))

# Step 6: Convert Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # complete the tour by returning to the depot

# Calculate total travel cost
total_travel_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel.cmdlineLinel_cost)