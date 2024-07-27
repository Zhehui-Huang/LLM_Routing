import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from heapq import heappop, heappush
from itertools import combinations

# Define city coordinates
coordinates = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28),
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Compute the distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Compute the Minimum Spanning Tree (MST) using Prim's Algorithm
def prim_mst(distances):
    n = len(distances)
    in_tree = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    parent = [-1] * n
    mst_edges = []
    heap = [(0, 0)]  # cost, node
    
    while heap:
        cost, u = heappop(heap)
        if in_tree[u]:
            continue
        in_tree[u] = True
        if parent[u] != -1:
            mst_edges.append((parent[u], u))
        
        for v in range(n):
            if not in_tree[v] and distances[u, v] < min_edge[v]:
                min_edge[v] = distances[u, v]
                parent[v] = u
                heappush(heap, (distances[u, v], v))
    
    return mst_edges

mst = prim_mst(distance_matrix)

# Find vertices with an odd degree in MST
degree = [0] * n_cities
for u, v in mst:
    degree[u] += 1
    degree[v] += 1

odd_vertices = [v for v in range(n_cities) if degree[v] % 2 == 1]

# Find the Minimum Weight Perfect Matching (MWPM) for odd-degree vertices
G_odd = nx.Graph()
G_odd.add_nodes_from(odd_vertices)
for u, v in combinations(odd_vertices, 2):
    G_odd.add_edge(u, v, weight=distance_matrix[u, v])
matching = nx.algorithms.matching.min_weight_matching(G_odd, maxcardinality=True, weight='weight')

# Combine edges of MST and Matching
multi_graph = nx.MultiGraph()
multi_graph.add_edges_from(mst)
multi_graph.add_edges_from(matching)

# Find the Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian Circuit to Hamiltonian Circuit (shortcut method)
visited = set()
hamiltonian_circuit = []
total_cost = 0
last_city = 0

for u, v in euler_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
        total_cost += distance_matrix[last_city, v]
        last_city = v

# Adding the return to the start
hamiltonian_circuit.append(0)
total_cost += distance_matrix[last_city, 0]

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)