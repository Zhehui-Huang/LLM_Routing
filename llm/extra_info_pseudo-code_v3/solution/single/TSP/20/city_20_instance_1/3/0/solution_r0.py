import math
import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from networkx.algorithms import eulerian_circuit
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
dist_matrix = np.array([[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)])

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

# Step 3: Find a minimum-weight perfect matching in the subgraph induced by O
complete_graph = nx.Graph()
for i in O:
    for j in O:
        if i != j:
            complete_graph.add_edge(i, j, weight=dist_matrix[i][j])
matching = nx.algorithms.matching.min_weight_matching(complete_graph, maxcardinality=True)

# Adding match edges to the graph
for edge in matching:
    G.add_edge(*edge, weight=dist_matrix[edge[0]][edge[1]])

# Step 5: Find an Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(G, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Adding the depot city again for return

# Calculate total travel cost for the Hamiltonian circuit
total_travel_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)