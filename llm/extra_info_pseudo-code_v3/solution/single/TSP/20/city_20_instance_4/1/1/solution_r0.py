import math
import networkx as nx
from itertools import combinations

# Function to calculate the Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# List of cities and their coordinates
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
          (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
          (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
          (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Create a complete graph where nodes are cities and weights are Euclidean distances
def create_complete_graph(cities):
    G = nx.Graph()
    for i, coord1 in enumerate(cities):
        for j, coord2 in enumerate(cities):
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(coord1, coord2))
    return G

# Function to find the Minimum Spanning Tree (MST) using Prim's algorithm
def minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G)

# Function to get vertices with odd degree in the tree
def odd_degree_vertices(T):
    return [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Function to find the Minimum Weight Perfect Matching in the subgraph
def minimum_weight_perfect_matching(G, O):
    subgraph = G.subgraph(O)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight="weight")

# Function to find an Eulerian circuit in the graph
def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

# Function to make an Eulerian tour into a Hamiltonian circuit by shortcutting duplicate visits
def make_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if not visited or v not in visited:
            path.append(v)
            visited.add(v)
    path.append(path[0])  # return to the starting node
    return path

# Christofides algorithm
def christofides_algorithm(cities):
    G = create_complete_graph(cities)
    T = minimum_spanning_tree(G)
    O = odd_degree_vertices(T)
    M = minimum_weight_perfect_matching(G, O)
    H = nx.MultiGraph(T)
    H.add_edges_from(M)
    eulerian_circuit = find_eulerian_circuit(H)
    hamiltonian_circuit = make_hamiltonian_circuit(eulerian_circuit)

    # Calculate total travel cost
    cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))
    return hamiltonian_circuit, cost

# Get the solution
tour, total_cost = christofides_algorithm(cities)

# Outputting the results
print("Tour:", tour)
print("Total travel cost:", total_cost)