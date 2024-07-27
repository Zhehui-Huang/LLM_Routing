import math
import networkx as nx
from itertools import combinations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def create_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def find_minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G)

def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

def find_minimum_weight_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

def form_multigraph(T, M):
    G = nx.MultiGraph(T)
    G.add_edges_from(M)
    return G

def find_eulerian_circuit(G):
    return list(nx.eulerian_circuit(G))

def make_hamiltonian_circuit(circuit):
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # return to the depot
    return path

def calculate_total_cost(path, cities):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += euclidean_distance(cities[path[i]], cities[path[i + 1]])
    return total_cost

def christofides(cities):
    G = create_graph(cities)
    T = find_minimum_spanning_tree(G)
    O = find_odd_degree_vertices(T)
    M = find_minimum_weight_matching(G, O)
    H = form_multigraph(T, M)
    circuit = find_eulerian_circuit(H)
    path = make_hamiltonian_circuit(circuit)
    total_cost = calculate_total_cost(path, cities)
    return path, total_cost

# Define the cities
cities = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Get the shortest tour and the total travel cost
tour, total_cost = christofides(cities)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")