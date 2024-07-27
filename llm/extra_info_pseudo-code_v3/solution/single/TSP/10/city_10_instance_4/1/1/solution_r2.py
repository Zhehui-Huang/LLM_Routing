import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
from networkx.algorithms import approximation

# Function to compute the Euclidean distance matrix
def compute_distances(points):
    n = len(points)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(points[i], points[j])
    return dist_matrix

# Construct the minimum spanning tree
def minimum_spanning_tree_full(n, dist_matrix):
    G = nx.Graph()
    for i in range(n):
        for j in range(n):
            if i != j:
        G.add_edge(i, j, weight=dist_matrix[i][j])
    return nx.minimum_spanning_tree(G)

# Convert MST to multigraph by adding a minimum weight matching of odd nodes
def add_min_weight_matching(mst, original_graph):
    odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]
    minimum_weight_matching = nx.algorithms.matching.min_weight_matching(original_graph.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')
    mst.add_edges_from(minimum_weight_matching)
    return mst

def eulerian_to_hamiltonian(path):
    seen = set()
    hamiltonian_path = []
    for node in path:
        if node not in seen:
            hamiltonian_path.append(node)
            seen.add(node)
    hamiltonian_path.append(hamiltonian_path[0])
    return hamiltonian_path

def compute_total_distance(path, dist_matrix):
    return sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))

def christofides_algorithm(cities):
    # Calculate distance matrix
    dist_matrix = compute_distances(cities)
    n = len(cities)
    # Step 1: Create a graph and compute MST
    graph = nx.Graph()
    for i in range(n):
        for j in range(n):
            if i != j:
                graph.add_edge(i, j, weight=dist_width_matrix[i][j])
    mst = nx.minimum_spanning_tree(graph)
    
    # Step 2: Minimum weight perfect matching on the odd degree vertices of the MST
    multigraph = add_min_weight_matching(mst, graph)
    
    # Step 3: Find Eulerian circuit
    euler_circuit = list(nx.eulerian_circuit(multigraph, source=0))
    
    # Step 4: Make Hamiltonian circuit
    hamiltonian_circuit = eulerian_to_hamiltonian([u for u, v in euler_circuit])
    
    # Calculate total travel cost
    total_cost = compute_total_distance(hamiltonian_circuit, dist_matrix)
    
    return hamiltonian_circuit, total_cost

# City coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
tour, cost = christofides_algorithm(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")