import math
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt

# Calculate distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with weights as distances
def create_complete_graph(cities):
    G = nx.Graph()
    for i, coord1 in cities.items():
        for j, coord2 in cities.items():
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(coord1, coord2))
    return G

# Compute the minimum weight perfect matching on odd degree vertices
def min_weight_perfect_matching(G, odd_verts):
    # Generate all pair combinations of odd degree vertices
    min_weight_matching = {}
    while odd_verts:
        v = odd_verts.pop()
        distance, u = min((G[v][w]['weight'], w) for w in odd_verts)
        odd_verts.remove(u)
        min_weight_matching[v] = u
    return min_weight_matching

# Find the Eulerian circuit on a graph
def find_eulerian_circuit(G, source):
    return list(nx.eulerian_circuit(G, source=source))

# Christofides Algorithm Implementation
def christofides_algorithm(cities):
    # Create a complete graph
    G = create_complete_graph(cities)
    
    # Step 1: Compute a minimum spanning tree T
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices of odd degree
    odd_degree_vertices = [v for v, d in T.degree() if d % 2 == 1]
    
    # Step 3: Find minimum-weight perfect matching M in the subgraph induced by odd vertices
    matching = min_weight_perfect_matching(G, odd_degree_vertices)
    
    # Add edges from the matching to the tree
    for u, v in matching.items():
        T.add_edge(u, v, weight=G[u][v]['weight'])

    # Step 5: Find an Eulerian circuit in the combined graph
    eulerian_circuit = find_eulerian_circuit(T, source=0)
    
    # Step 6: Make the circuit Hamiltonian, remove repeated nodes
    visited = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(0)  # adding the depot city again to complete the tour

    # Calculate total cost
    total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))
    
    return hamiltonian_circuit, total_cost

# Calculate shortest tour using Christofides algorithm
tour, cost = christofides_algorithm(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")