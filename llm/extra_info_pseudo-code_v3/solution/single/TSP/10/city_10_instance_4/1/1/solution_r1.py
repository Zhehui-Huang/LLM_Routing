import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
import itertools

# Function to compute Euclidean distance matrix
def compute_distances(points):
    n = len(points)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(points[i], points[j])
    return dist_matrix

# Create graph from distance matrix
def create_graph(dist_matrix):
    G = nx.Graph()
    size = len(dist_matrix)
    for i in range(size):
        for j in range(i + 1, size):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

# Find minimum weight perfect matching for odd degree vertices
def min_weight_perfect_matching(G, vertices):
    min_matching = nx.Graph()
    odd_graph = G.subgraph(vertices)
    matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')
    min_matching.add_edges_from(matching)
    return min_matching

# Convert Eulerian circuit to Hamiltonian path
def eulerian_to_hamiltonian(circuit):
    path, seen = [], set()
    for u, v in circuit:
        if u not in seen:
            path.append(u)
            seen.add(u)
    path.append(path[0])
    return path

# Function for Christofides' algorithm
def christofides(points):
    # Compute all-pairs distances
    dist_matrix = compute_distances(points)
    G = create_graph(dist_matrix)
    
    # Step 1: Minimum spanning tree
    mst_tree = nx.minimum_spanning_tree(G)
    
    # Step 2: Vertices with odd degree
    odd_vertices = [v for v, deg in mst_tree.degree() if deg % 2 == 1]
    
    # Step 3: Minimum perfect matching on odd vertices
    mpm_matching = min_weight_perfect_matching(G, odd_vertices)
    
    # Step 4: Combine MST and matching
    multigraph = nx.MultiGraph(mst_tree)
    multigraph.add_edges_from(mpm_matching.edges())
    
    # Step 5: Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))
    
    # Step 6: Convert to Hamiltonian path
    hamiltonian_path = eulerian_to_hamiltonian(eulerixn_circuit)
    
    # Compute tour cost
    tour_cost = sum(dist_matrix[u][v] for u, v in zip(hamiltonian_path[:-1], hamiltonian_path[1:]))
    return hamiltonian_path, tour_cost

# City coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Running Christofides' algorithm to find the tour
tour, cost = christofides(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")