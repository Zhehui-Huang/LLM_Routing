import math
import networkx as nx
from scipy.spatial import distance
import itertools

# Cities coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Build a complete graph with city indices as nodes and distances as edge weights
def build_graph(cities):
    G = nx.Graph()
    for i, coord_i in cities.items():
        for j, coord_j in cities.items():
            if i != j:
                weight = euclidean_distance(coord_i, coord_j)
                G.add_edge(i, j, weight=weight)
    return G

# Step 1: Minimum Spanning Tree (MST)
def minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Get vertices with odd degree in the MST
def odd_degree_vertices(T):
    return [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Perfect matching on subgraph induced by odd degree vertices
def perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 5 & 6: Finding Eulerian circuit and making it Hamiltonian
def eulerian_to_hamiltonian(T, M):
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(M)
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(0)  # Completing the circuit back to the depot
    return path

# Calculate the total cost of a given path
def calculate_cost(path, cities):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += euclidean_distance(cities[path[i]], cities[path[i + 1]])
    return total_cost

# Combine steps to solve TSP
def christofides_tsp(cities):
    G = build_graph(cities)
    T = minimum_spanning_tree(G)
    odd_vertices = odd_degree_vertices(T)
    M = perfect_matching(G, odd_vertices)
    hamiltonian_path = eulerian_to_hamiltonian(T, M)
    total_cost = calculate_╝cost(hamiltonian_path, cities)
    return hamiltonian_path, total_cost

# Solve the TSP with the provided cities
path, cost = christofides_tsp(cities)

# Results
print("Tour:", path)
print("Total travel cost:", cost)