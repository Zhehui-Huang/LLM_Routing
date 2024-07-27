import numpy as np
import networkx as nx
from itertools import combinations

# Define the cities
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def build_complete_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def compute_mst(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

def min_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def form_multigraph(T, matching):
    multigraph = nx.MultiGraph(T)
    for u, v in matching:
        multigraph.add_edge(u, v, weight=euclidean_distance(cities[u], cities[v]))
    return multigraph

def find_eulerian_circuit(multigraph):
    return list(nx.eulerian_circuit(multigraph))

def convert_to_hamiltonian_circuit(circuit, start_node):
    path = [start_node]
    visited = set(path)
    for u, v in circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(start_node)
    return path

def calculate_total_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += euclidean_distance(cities[path[i]], cities[path[i + 1]])
    return total_cost

# Apply Christofides algorithm
G = build_complete_graph(cities)
T = compute_mst(G)
odd_vertices = find_odd_degree_vertices(T)
matching = min_weight_perfect_matching(G, odd_vertices)
multigraph = form_multagraph(T, matching)
circuit = find_eulerian_circuit(multigraph)
tour = convert_to_hamiltonian_circuit(circuit, 0)
total_cost = calculate_total_cost(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)