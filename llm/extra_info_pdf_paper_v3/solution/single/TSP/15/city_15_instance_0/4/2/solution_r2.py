import numpy as np
import networkx as nx

# Coordinates of the cities including the depot city
coordinates = np.array([
    (9, 93),   # City 0 - Depot
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
])

def calculate_distance(coords1, coords2):
    return np.linalg.norm(np.array(coords1)-np.array(coords2))

# Create a distance matrix
def distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(coords[i], coords[j])
            dist/np.linalg.norm(coordinates[i]-coordinates[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

# Construct full graph on nodes using distance matrix
def full_graph(dist_matrix):
    n = len(dist_matrix)
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

def christofides_algorithm(G):
    # Step 1: Create a minimum spanning tree of G
    T = nx.minimum_spanning_tree(G, weight='weight')
    
    # Step 2: Find vertices with odd degree
    odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 != 0]
    
    # Step 3: Minimum weight perfect matching on the graph induced by odd-degree vertices
    odd_graph = nx.Graph(G.subgraph(odd_degree_nodes))
    min_weight_matching = nx.algorithms.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')
    
    # Step 4: Add edges of minimum weight matching to T
    T.add_edges_from(min_weight_matching)
    
    # Step 5: Find an Eulerian circuit in T
    eulerian_circuit = list(nx.eulerian_circuit(T, source=0))
    
    # Step 6: Make the circuit Hamiltonian
    visited = set()
    path = []
    cost = 0
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            path.append(v)
            if len(path) > 1:
                cost += G[path[-2]][path[-1]]['weight']
    path.append(0)  # Adding the depot to complete the tour
    cost += G[path[-2]][path[-1]]['weight']  # Add the return to the depot edge
    
    return path, cost

# Calculating the distance matrix
dist_matrix = distance_matrix(coordinates)

# Creating the full graph
G = full_graph(dist_matrix)

# Solving TSP using Christofides algorithm
tour, total_cost = christofides_algorithm(G)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)