import math
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Coordinates of cities including the depot city at index 0
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Calculating the Euclidean distances between each pair of cities
def calculate_distances(cities):
    dist_matrix = squareform(pdist(cities, 'euclidean'))
    return dist_matrix

# Construct a complete graph with weights (distances between cities)
def create_complete_graph(num_cities, dist_matrix):
    G = nx.Graph()
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

# Step 1: Compute a minimum spanning tree (MST) using Kruskal's algorithm
def compute_mst(G):
    return nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degrees in the MST
def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find a minimum-weight perfect matching for the odd degree vertices
def minimum_weight_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 4+5: Find an Eulerian circuit in the combined graph (MST + matching)
def find_eulerian_circuit(T, M):
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(M)
    return list(nx.eulerian_circuit(multigraph))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # return to the starting node
    return path

# Calculate total travel cost for the path
def calculate_cost(path, dist_matrix):
    cost = sum(dist_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
    return cost

# Solving the problem
dist_matrix = calculate_distances(cities)
G = create_complete_graph(len(cities), dist_matrix)
T = compute_mst(G)
odd_degree_vertices = find_odd_degree_vertices(T)
M = minimum_weight_matching(G, odd_degree_vertices)
eulerian_circuit = find_eulerian_circuit(T, M)
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)
total_cost = calculate_cost(hamiltonian_circuit, dist_matrix)

# Outputting the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")