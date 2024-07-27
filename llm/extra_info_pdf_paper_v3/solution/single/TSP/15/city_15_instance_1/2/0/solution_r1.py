import math
import networkx as nx
import numpy as np
from scipy.spatial.distance import pdist, squareform

def calculate_distances(cities):
    return squareform(pdist(cities))

def find_odd_degree_vertices(tree):
    return [v for v, d in tree.degree() if d % 2 == 1]

def minimum_cost_perfect_matching(odd_vertices, full_graph):
    graph = nx.Graph()
    for i in odd_vertices:
        for j in odd_vertices:
            if i != j:
                graph.add_edge(i, j, weight=full_graph[i][j])
    return nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)

def create_eulerian_circuit(graph, start_vertex):
    return list(nx.eulerian_circuit(nx.MultiGraph(graph), source=start_vertex))

def simplify_circuit(circuit):
    visited = set()
    path = []
    cost = 0
    
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        # Assuming bidirectional edges with the same cost
        cost += graph[u][v]
    
    path.append(start_vertex)  # complete the cycle by returning to the initial point
    return path, cost

cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (9, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

distances = calculate_distances(cities)

G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=distances[i][j])

# Step 1: Create MST
mst = nx.minimum_spanning_tree(G)

# Step 2: Find odd degree vertices in MST
odd_degree_vertices = find_odd_degree_vertices(mst)

# Step 3: Find minimum cost perfect matching
matching = minimum_cost_perfect_matching(odd_degree_vertices, G)

# Combine MST and matching to get an Eulerian circuit
for u, v in matching:
    mst.add_edge(u, v, weight=distances[u][v])

start_vertex = 0
eulerian_circuit = create_eulerian_circuit(mst, start_vertex)

# Convert Eulerian circuit to Hamiltonian cycle
tour, total_cost = simplify_circuit(eulerian_circuit)

print("Tour:", tour)
print("Total travel cost:", total_cost)