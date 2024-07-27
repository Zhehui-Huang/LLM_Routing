import math
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def min_weight_perfect_matching(G, odd_nodes):
    subgraph = G.subgraph(odd_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    return min_weight_matching

def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0])  # to form a cycle back to the starting node
    return hamiltonian_circuit

# Coordinates for each city
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Create a complete graph
G = nx.complete_graph(len(cities))
for i, j in combinations(range(len(cities)), 2):
    G.edges[i, j]['weight'] = euclidean_distance(cities[i], cities[j])

# Step 1: Compute the MST
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree
odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]

# Step 3: Find a minimum-weight perfect matching
M = min_weight_perfect_matching(G, odd_degree_nodes)

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = find_eulerian_circuit(H)

# Step 6: Convert Eulerian to Hamiltonian circuit
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)

# Calculate the total travel cost
total_cost = sum(G.edges[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)