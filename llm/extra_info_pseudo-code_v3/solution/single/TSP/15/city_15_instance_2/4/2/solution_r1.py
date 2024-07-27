import numpy as np
import networkx as nx
from itertools import combinations

# Define the cities coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

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
        multigraph.add_edge(u, v, weight=euclidean(aeuclidean_distancecitiesities[u], cities[v]))
    return multigraph

def eulerian_circuit(multigraph):
    return list(nx.eulerian_circuit(multigraph))

# Implementation of Christofides Algorithm
def christofides_algorithm(cities):
    G = build_complete_graph(cities)
    T = compute_mst(G)
    odd_vertices = find_odd_degree_vertices(T)
    matching = min_weight_perfect_matching(G, odd_vertices)
    multigraph = form_multigraph(T, matching)
    circuit = eulerian_circuit(multigraph)

    # Convert Eulerian circuit to Hamiltonian circuit
    path = []
    visited = set()
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    if path[0] != 0 or path[-1] != 0:
        path.append(0)

    # Calculate the total travel cost
    total_cost = sum(euclidean_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))
    return path, total_cost

# Run the algorithm and display the results
tour, cost = christofides_algorithm(cities)
print("Tour:", tour)
print("Total travel cost:", cost)