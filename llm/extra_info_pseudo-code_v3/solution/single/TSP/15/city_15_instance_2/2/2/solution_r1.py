import math
import networkx as nx
from itertools import combinations

# Coordinates of cities, indexed from 0 to 14
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_complete_graph(coords):
    G = nx.Graph()
    n = len(coords)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coords[i], coords[j])
            G.add_edge(i, j, weight=dist)
    return G

def minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def get_odd_degree_vertices(T):
    return [v for v, degree in T.degree() if degree % 2 != 0]

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def create_multigraph(T, M):
    G = nx.MultiGraph(T)
    for u, v in M:
        G.add_edge(u, v, weight=G[u][v][0]['weight'])  # assume original weight is carried over
    return G

def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to complete the cycle
    return path

def calculate_tour_cost(path, G):
    total_cost = 0
    for i in range(1, len(path)):
        u, v = path[i-1], path[i]
        total_cost += G[u][v][0]['weight']
    return total_cost

# Main Flow
G = create_complete_graph(coordinates)
T = minimum_spanning_tree(G)
O = get_odd_degree_vertices(T)
M = minimum_weight_perfect_matching(G, O)
H = create_multigraph(T, M)
eulerian_circuit = find_eulerian_circuit(H)
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)
total_cost = calculate_tour_cost(hamiltonian_circuit, G)

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)