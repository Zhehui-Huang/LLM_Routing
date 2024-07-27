import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Cities coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with weights as distances
def create_complete_graph(cities):
    n = len(cities)
    adj_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                adj_matrix[i][j] = float('inf')
    return adj_matrix

# Step 1: Compute a minimum spanning tree (MST) of G
def compute_mst(graph):
    mst_matrix = minimum_spanning_tree(csr_matrix(graph)).toarray()
    return mst_matrix

# Helper function to get odd degree vertices from MST
def get_odd_degree_vertices(mst):
    odd_vertices = []
    degrees = [sum(1 for x in row if x > 0) for row in mst]
    for i, degree in enumerate(degrees):
        if degree % 2 != 0:
            odd_vertices.append(i)
    return odd_vertices

# Step 3: Minimum-weight perfect matching
def minimum_weight_perfect_matching(graph, odd_vertices):
    g = nx.Graph()
    g.add_nodes_from(odd_vertices)
    for i in odd_vertices:
        for j in odd_vertices:
            if i != j:
                g.add_edge(i, j, weight=graph[i][j])
    matching = nx.algorithms.matching.min_weight_matching(g, maxcardinality=True)
    return matching

# Step 5 & 6: Find Eulerian circuit and convert to Hamiltonian circuit
def find_eulerian_circuit(mst, matching):
    multigraph = nx.Graph()
    multigraph.add_weighted_edges_from((i, j, mst[i][j]) for i in range(len(mst)) for j in range(len(mst)) if mst[i][j] > 0)
    multigraph.add_edges_from(matching)
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))
    return eulerian_circuit

# Function to Convert Eulerian to Hamiltonian
def eulerian_to_hamiltonian(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # adding the start point to end to complete the circuit.
    return path

# Main function to integrate all steps
def christofides_tsp(cities):
    graph = create_complete_graph(cities)
    mst = compute_mst(graph)
    odd_vertices = get_odd_degree_vertices(mst)
    matching = minimum_weight_perfect_matching(graph, odd_vertices)
    eulerian_circuit = find_eulerian_circuit(mst, matching)
    hamiltonian_circuit = eulerian_to_hamiltonian(eulerian_circuit)
    
    # Calculate total travel cost
    total_travel_cost = sum(graph[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))
    
    return hamiltonian_circuit, total_travel_cost

# Execute the algorithm
tour, cost = christofides_tsp(cities)
print("Tour:", tour)
print("Total travel cost:", cost)