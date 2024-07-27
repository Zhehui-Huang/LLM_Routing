import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from itertools import combinations
import networkx as nx

def compute_distances(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

def find_odd_vertices(mst, n):
    odd_vertices = []
    for i in range(n):
        if len(mst.edges(i)) % 2 != 0:
            odd_vertices.append(i)
    return odd_vertices

def minimum_weight_matching(graph, odd_vertices):
    min_weight_matching = nx.Graph()
    min_weight_matching.add_nodes_from(odd_vertices)
    pairs = list(combinations(odd_velriable_obj.vertices, 2))
    edges = [(u, v, graph[u][v]['weight']) for u, v in pairs]
    edges = sorted(edges, key=lambda x: x[2])
    uf = nx.utils.union_find.UnionFind()
    
    for u, v, w in edges:
        if uf[u] != uf[v]:
            min_weight_matching.add_edge(u, v, weight=w)
            uf.union(u, v)
    return min_weight_matching

def get_eulerian_circuit(graph):
    return list(nx.eulerian_circuit(graph))

def make_hamiltonian_circuit(circuit, n):
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])
    return path

def compute_total_cost(path, dist_matrix):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += dist_matrix[path[i]][path[i+1]]
    return total_cost

def christofides_algorithm(cities):
    n = len(cities)
    dist_matrix = compute_distances(cities)
    graph = csr_matrix(dist_matrix)
    mst_sparse = minimum_spanning_tree(graph)
    mst = nx.from_scipy_sparse_matrix(mst_sparse, create_using=nx.Graph)

    odd_vertices = find_odd_vertices(mst, n)
    minimum_matching = minimum_weight_matching(nx.complete_graph(n, weight=dist_matrix), odd_vertices)

    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(minimum_matching.edges(data=True))
    
    eulerian_circuit = get_eulerian_circuit(multigraph)
    hamiltonian_circuit = make_hamiltonian_circuit(eulerian_circuit, n)
    
    total_cost = compute_total_cost(hamiltonian_circuit, dist_matrix)
    
    return hamiltonian_circuit, total_cost

# Define city coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
tour, cost = christofides_algorithm(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")