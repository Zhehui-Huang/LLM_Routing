import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms import approximation as approx

def euclidean_distance(coords1, coords2):
    """Calculate euclidean distance between two points."""
    return np.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)

def form_full_graph(cities):
    """ Create a complete graph from city coordinates with distances as edge weights."""
    n = len(cities)
    G = nx.Graph()
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

def find_approx_tsp_tour(cities):
    # Create graph
    G = form_full_graph(cities)
    
    # Step 1: Minimum Spanning Tree
    MST = nx.minimum_spanning_tree(G, weight='weight')
    
    # Step 2: Get vertices of odd degree in MST
    odd_vertices = [v for v, degree in MST.degree() if degree % 2 == 1]
    
    # Step 3: Minimum weight perfect matching in the induced subgraph on odd degree vertices
    induced_subgraph = G.subgraph(odd_vertices)
    matching = approx.min_weight_matching(induced_subgraph, maxcardinality=True, weight='weight')
    
    # Step 4: Combine the edges of MST and matching to form a multigraph
    multi_G = nx.MultiGraph(MST)
    for edge in matching:
        multi_G.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]]['weight'])
    
    # Step 5: Find an Eulerian circuit in the multigraph
    eulerian_circuit = nx.eulerian_circuit(multi_G, source=0)
    
    # Step 6: Make a Hamiltonian circuit by visiting cities only once
    visited = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_circuit.append(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0])

    # Calculate the total cost
    total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1))
    
    return hamiltonian_circuit, total_cost

# City coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Find the TSP tour using Christofides' algorithm
tour, total_cost = find_approx_tsp_tour(cities)

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))