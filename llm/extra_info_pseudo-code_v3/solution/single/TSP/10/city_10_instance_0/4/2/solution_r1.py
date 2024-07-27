import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms import matching, tree

def calculate_euclidean_distance(points):
    return distance_matrix(points, points)

def find_mst_and_odd_vertices(G):
    # Generating MST of the graph
    mst = tree.minimum_spanning_tree(G, algorithm='kruskal', weight='weight')
    # Finding vertices with odd degree in MST
    odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]
    return mst, odd_degree_nodes

def minimum_weight_perfect_matching(G, odd_degree_nodes):
    # Generate subgraph over odd degree nodes
    subgraph = G.subgraph(odd_degree_nodes)
    # Calculate the minimum weight perfect matching
    mwpm = matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return mwpm

def create_multigraph(H, M):
    multigraph = nx.MultiGraph(H)
    multigraph.add_edges_from(M)
    return multigraph

def find_eulerian_circuit(multigraph):
    # Find Eulerian circuit
    return list(nx.eulerian_circuit(multigraph))

def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # To make it a circuit
    return path

def christofides_algorithm(cities):
    G = nx.complete_graph(len(cities))
    distances = calculate_euclidean_distance(cities)
    for i, j in itertools.combinations(range(len(cities)), 2):
        G[i][j]['weight'] = distances[i][j]

    T, odd_vertices = find_mst_and_odd_vertices(G)
    M = minimum_weight_perfect_matching(G, odd_vertices)
    H = create_multigraph(T, M)
    eulerian_circuit = find_eulerian_circuit(H)
    tour = create_hamiltonian_circuit(eulerian_circuit)
    
    # Calculate tour cost
    tour_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    
    return tour, tour_cost

# Define the coordinates of the cities
cities = np.array([
    (50, 42), # Depot
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
])

tour, tour_cost = christofides_algorithm(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")