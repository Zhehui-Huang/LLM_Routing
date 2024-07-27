import math
import networkx as nx
from scipy.optimize import linear_sum_assignment

# Define the cities
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create the distance matrix
n = len(cities)
distance_matrix = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Build the MST using Kruskal's algorithm
G = nx.Graph()
for i in range(n):
    for j in range(i+1, n):
        G.add_edge(i, j, weight=distance_matrix[i][j])
mst = nx.minimum_spanning_tree(G)

# Find vertices of odd degree
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Minimum Cost Perfect Matching on the odd-degree nodes
induced_subgraph = G.subgraph(odd_degree_nodes)
odd_graph_weight_matrix = nx.to_numpy_array(induced_subgraph)
row_ind, col_ind = linear_sum_assignment(odd_graph_weight_matrix)
matching = nx.Graph()
for i, j in zip(row_ind, col_ind):
    matching.add_edge(odd_degree_nodes[i], odd_degree_nodes[j], weight=odd_graph_weight_matrix[i][j])

# Multigraph to combine MST and Matching to get a Eulerian graph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching.edges())

# Find the Eulerian Circuit, this circuit will visit some nodes multiple time
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian Circuit to a Hamiltonian Circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = [0]  # starting and ending at the depot
total_cost = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        if v != 0:  # do not add to visited if it's the return to depot
            visited.add(v)
        if hamiltonian_circuit[-1] != v:  # to avoid direct loop back in path description
            hamiltonian_circuit.append(v)
            total_cost += distance_matrix[hamiltonian_circuit[-2]][v]

# add the return to depot cost
hamiltonian_circuit.append(0)
total_cost += distance_matrix[hamiltonian_circuit[-2]][0]

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)