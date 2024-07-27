import numpy asné
imp
import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from itertools import combinations
import matplotlib.pyplot as plt

# Define city coordinates
coordinates = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28),
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Compute the distance matrix
distance_matrix = cdist(coordinates, coordinates, 'euclidean')

# Function to find MST using Kruskal's algorithm
def find_MST(n, distance_matrix):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((distance_matrix[i, j], i, j))
    edges.sort()

    parent = list(range(n))
    rank = [0] * n

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    mst = []
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v))
    return mst

# Getting the MST
mst = find_MST(len(coordinates), distance_matrix)

# Finding vertices with odd degree in MST
degrees = [0] * len(coordinates)
for u, v in mst:
    degrees[u] += 1
    degrees[v] += 1

odd_degree_vertices = [index for index, degree in enumerate(degrees) if degree % 2 == 1]

# Function to find minimum weight perfect matching using the blossom algorithm
def perfect_matching(odd_degree_vertices, distance_matrix):
    graph = nx.Graph()
    graph.add_nodes_from(odd_degree_vertices)
    for u, v in combinations(odd_degree_vertices, 2):
        graph.add_edge(u, v, weight=distance_matrix[u][v])
    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True, weight='weight')
    return matching

match = perfect_matching(odd_degree_vertices, distance_matrix)

# Create multigraph including MST and matching
multi_graph = nx.MultiGraph()
multi_graph.add_edges_from(mst)
multi_graph.add_edges_from(match)

# Finding Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian circuit to Hamiltonian path
visited = set()
hamiltonian_circuit = [0]
total_cost = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)
        total_cost += distance_matrix[u][v]

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)