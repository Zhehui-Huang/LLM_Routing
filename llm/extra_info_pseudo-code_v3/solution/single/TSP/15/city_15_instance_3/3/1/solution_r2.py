import numpy as np
import networkx as nx

def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np. array(city2))

# Create the distance matrix
def compute_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = calculate_distance(cities[i], cities[j])
    return dist_matrix

# Christofides algorithm step by step
def christofides_algorithm(cities):
    num_cities = len(cities)
    dist_matrix = compute_distances(cities)

    # Create graph and compute MST
    G = nx.Graph()
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    mst = nx.minimum_spanning_tree(G)

    # Find vertices of odd degree
    odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

    # Create subgraph with odd degree vertices and find minimum weight perfect matching
    min_weight_subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(min_weight_subgraph, maxcardinality=True)

    # Combine MST and matching to get a multigraph
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(min_weight_matching)

    # Find an Eulerian circuit
    euler_circuit = list(nx.eulerian_circuit(multigraph, source=0))

    # Convert Eulerian circuit to Hamiltonian path
    visited = set()
    path = []
    for u, v in euler_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # completing the circuit

    # Calculate the total path cost
    total_cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))

    return path, total_cost

# Coordinates of all cities including the depot
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
          (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
          (70, 95), (29, 64), (32, 79)]

# Running Christofides algorithm to get the tour and cost
tour, total_cost = christofides_algorithm(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)