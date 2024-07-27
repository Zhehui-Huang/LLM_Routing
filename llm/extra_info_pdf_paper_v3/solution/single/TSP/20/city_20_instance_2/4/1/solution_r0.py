import math
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment
import networkx as nx
import numpy as np

# Step 1. Prepare the data for cities
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate the distance matrix
dist_matrix = distance_matrix(cities, cities)

# Step 2. Construct the Minimum Spanning Tree (MST)
def mst_prim(matrix):
    num_vertices = len(matrix)
    selected = [False] * num_vertices
    selected[0] = True
    mst_edges = []

    while len(mst_edges) < num_vertices - 1:
        min_edge = (None, None, float('inf'))
        for u in range(num_vertices):
            if selected[u]:
                for v in range(num_vertices):
                    if not selected[v] and matrix[u][v] < min_edge[2]:
                        min_edge = (u, v, matrix[u][v])
        mst_edges.append(min_edge)
        selected[min_edge[1]] = True
    return mst_edges

mst_tree = mst_prim(dist_matrix)

# Step 3. Create a graph from the MST
G = nx.Graph()
G.add_weighted_edges_from(mst_tree)

# Step 4. Find minimum-cost perfect matching in the subgraph of odd-degree vertices
odd_degree_nodes = [node for node in G.nodes if G.degree(node) % 2 == 1]
odd_graph = nx.Graph()
odd_graph.add_weighted_edges_from([(u, v, dist_matrix[u][v]) for u in odd_degree_nodes for v in odd_degree_nodes if u != v])
min_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add matching edges to the graph
G.add_edges_from(min_matching)

# Step 5. Find Eulerian circuit and then make it a Hamiltonian path
eulerian_circuit = list(nx.algorithms.eulerian_circuit(G, source=0))
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Close the tour
hamiltonian_circuit.append(0)

# Compute total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)