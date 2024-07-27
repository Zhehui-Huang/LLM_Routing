import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

def create_graph(num_cities, distances):
    G = nx.Graph()
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                G.add_edge(i, j, weight=distances[i, j])
    return G

def find_mst(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def find_odd_degree_vertices(G):
    return [v for v in G.nodes() if G.degree(v) % 2 != 0]

def add_minimum_weight_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    matching = nx.algorithms.min_weight_matching(subgraph, maxcardinality=True)
    for edge in matching:
        G.add_edge(edge[0], edge[1])

def find_eulerian_circuit(G, start_vertex):
    return list(nx.eulerian_circuit(G, source=start_vertex))

def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_circuit.append(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0])  # make it a cycle
    return hamiltonian_circuit

def calculate_tour_cost(circuit, distance_matrix):
    total_cost = 0
    for i in range(len(circuit) - 1):
        total_cost += distance_matrix[circuit[i], circuit[i+1]]
    return total_cost

# Define cities coordinates
cities = np.array([
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
])

# Calculate distance matrix
distance_matrix = squareform(pdist(cities))

# Create graph and perform algorithm steps
G = create_graph(len(cities), distance_matrix)
mst = find_mst(G)
odd_vertices = find_odd_degree_vertices(mst)
add_minimum_weight_matching(mst, odd_vertices)
eulerian_circuit = find_eulerian_circuit(mst, 0)
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)
total_cost = calculate_tour_cost(hamiltonian_circuit, distance_matrix)

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)