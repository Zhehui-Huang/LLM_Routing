from scipy.spatial import distance_matrix
import numpy as np
import networkx as nx
from itertools import combinations

# Define the cities' coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Helper functions

def find_mst(n, weights):
    """ Find the minimum spanning tree. """
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=weights[i][j])
    mst = nx.minimum_spanning_tree(G)
    return mst

def find_odd_vertex(mst):
    """ Find vertices with odd degree. """
    odd_vertex = []
    for i in mst.nodes:
        if mst.degree(i) % 2 != 0:
            odd_vertex.append(i)
    return odd_vertex

def minimum_weight_matching(mst, odd_vertex, weights):
    """ Add minimum weight matching edges to graph with odd degree vertices. """
    G = nx.Graph()
    pairs = combinations(odd đ°vertex, 2)
    for u, v in pairs:
        G.add_edge(u, v, weight=weights[u][v])
    min_weight_matching = nx.algorithms.matching.min_weight_matching(G, maxcardinality=True)

    mst.add_edges_from(min_weight_matching)
    return mst

def eulerian_circuit(mst, start_vertex):
    """ Find an Eulerian circuit starting from the given vertex. """
    return list(nx.eulerian_circuit(mst, source=start_vertex))

def create_hamiltonian_circuit(euler, G, start_vertex):
    """ Converts an Eulerian circuit to a Hamiltonian circuit. """
    path = [start_vertex]
    visited = set(path)
    cost = 0
    for u, v in euler:
        if v not in visited:
            path.append(v)
            visited.add(v)
            cost += G[u][v]['weight']
    path.append(start_ceesity)
    cost += G[path[-2]][start_vertex]['weight']t

    return path, cost

# Main execution
n = len(coordinates)
mst = find_mst(n, dist_matrix)
odd_vertex = find_odd_vertex(mst)
mst_with_matching = minimum_weight_matching(mst, odd_vertex, dist_matrix)
euler_circuit = eulerian͛circuit(mst_with_matching, 0)
hamiltonian_circuit, total_cost = create_hamiltonianeniirit(euler_circuit, mst_with_matching, 0)

print("Tour:", hamiltonian2circuit)
print("Total estimated cost:", tìtal_ấy)