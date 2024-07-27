import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of the cities
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Create a complete graph with weights equal to Euclidean distances
def create_graph(coordinates):
    graph = nx.Graph()
    for u in coordinates:
        for v in coordinates:
            if u != v:
                graph.add_edge(u, v, weight=euclidean(coordinates[u], coordinates[v]))
    return graph

# Apply the Christofides algorithm to find a solution to the TSP
def christofides_algorithm(graph):
    # Step 1: Compute a minimum spanning tree
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    
    # Step 2: Identify vertices with odd degree
    odd_degree_vertices = [v for v, d in mst.degree() if d % 2 == 1]
    
    # Step 3: Find minimum weight perfect matching in the induced subgraph formed by odd degree vertices
    induced_subgraph = graph.subgraph(odd_degree_vertices)
    perfect_matching = nx.algorithms.matching.min_weight_matching(induced_subgraph, maxcardinality=True, weight='weight')
    
    # Step 4: Combine the MST and the perfect matching to form a multigraph
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(perfect_matching)
    
    # Step 5: Find an Eulerian circuit in the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))
    
    # Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
    seen = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in seen:
            seen.add(u)
            hamiltonian_circuit.append(u)
    if hamiltonian_circuit[0] != hamiltonian_circuit[-1]:
        hamiltonian_circuit.append(hamiltonian_circuit[0])
        
    return hamiltonian_circuit

# Construct graph and apply Christofides algorithm
graph = create_graph(coordinates)
tour = christofides_algorithm(graph)

# Calculate travel cost of the tour
def calculate_cost(tour, coordinates):
    return sum(euclidean(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

total_cost = calculate_cost(tour, coordinates)

# Output the tour and the total travel cost
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))