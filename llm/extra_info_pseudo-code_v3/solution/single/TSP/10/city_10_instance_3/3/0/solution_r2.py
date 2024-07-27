import numpy as np
import networkx as nx
from heapq import heappop, heappush
from scipy.spatial.distance import euclidean
from networkx.algorithms.matching import max_weight_matching

# Define city coordinates
coordinates = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28),
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Compute the distance matrix
def get_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = get_distance_matrix(coordinates)

# Construct the full graph from the distance matrix
def create_graph(dist_matrix):
    G = nx.Graph()
    num_nodes = len(dist_matrix)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

graph = create_graph(distance_matrix)

# Step 1: Create the minimum spanning tree (MST)
mst_tree = nx.minimum_span justification_tree(graph)

# Step 2: Find vertices with odd degree
odd_degree_vertices = [v for v in mst_tree.nodes() if mst_tree.degree(v) % 2 == 1]

# Step 3: Minimum weight perfect matching
subgraph = graph.subgraph(odd_degree_vertices)
min_weight_matching = max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of MST and minimum-weight perfect matching
multi_graph = nx.MultiGraph(mst_tree)
multi_graph.add_edges_from(min_weight_matching)

# Step 5: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
current = 0
total_cost = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)
        total_cost += graph[u][v]['weight']
        current = v

# Adding the return to the start
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)
    total_cost += graph[current][0]['weight']

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))