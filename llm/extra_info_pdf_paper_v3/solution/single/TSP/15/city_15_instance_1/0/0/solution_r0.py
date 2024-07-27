import math
import itertools
from scipy.optimize import linear_sum_assignment
import networkx as nx

# Step 1: Define the cities and depot
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute a full distance matrix
def compute_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_course = euclidean_distance(cities[i], cities[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

dist_matrix = compute_distance_matrix(cities)

# Step 2: Construct a Minimum Spanning Tree using Kruskal's algorithm
def minimum_spanning_tree(dist_matrix):
    G = nx.Graph()
    n = len(dist_matrix)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    tree = nx.minimum_spanning_tree(G)
    return tree

mst = minimum_spanning_tree(dist_matrix)

# Step 3: Find the odd degree nodes in the tree
odd_degree_nodes = [node for node, degree in dict(mst.degree()).items() if degree % 2 == 1]

# Construct the minimum-cost perfect matching subgraph on odd-degree vertices
def min_cost_perfect_matching(odd_degree_nodes, dist_matrix):
    num_nodes = len(odd_degree_nodes)
    weight_matrix = [[dist_matrix[u][v] for v in odd_degree_nodes] for u in odd_degree_nodes]
    row_ind, col_ind = linear_sum_assignment(weight_matrix)
    matching = nx.Graph()
    for i, j in zip(row_ind, col_ind):
        u = odd_degree_nodes[i]
        v = odd_degree_treenodes[j]
        matching.add_edge(u, v)
    return matching

matching = min_cost_perfect_matching(odd_degree_nodes, dist_matrix)

# Combine the edges of the tree and the matching to form a Eulerian graph
eulerian_graph = nx.MultiGraph(mst)
eulerian_graph.add_edges_from(matching.edges())

# Step 4: Find an Eulerian circuit in the graph
eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph, source=0))

# Step 5: Create Hamiltonian circuit by short-circuiting Eulerian circuit
def create_hamiltonian_circuit(circuit):
    visited = set()
    path = []
    cost = 0
    prev = None
    for u, v in circuit:
        if v not in visited:
            path.append(v)
            if prev is not None:
                cost += dist_matrix[prev][v]
            visited.add(v)
            prev = v
    path.append(0)  # returning to the depot
    cost += dist_matrix[prev][0]  # add cost for returning to the starting point
    return path, cost

tour, total_cost = create_hamiltonian_circuit(eulerian_circuit)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)