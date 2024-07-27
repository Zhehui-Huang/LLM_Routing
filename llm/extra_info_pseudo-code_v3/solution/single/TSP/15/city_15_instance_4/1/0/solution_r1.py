import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial.distance import euclidean
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# City coordinates with the depot city first
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Create a graph from the cities
def create_graph(cities):
    G = nx.Graph()
    for i, j in combinations(range(len(cities)), 2):
        G.add_edge(i, j, weight=euclidean(cities[i], cities[j]))
    return G

# Christofides' algorithm
def christofides_algorithm(G):
    # Step 1: Compute a minimum spanning tree
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices with odd degree
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]
    
    # Create subgraph of those nodes
    odd_subgraph = G.subgraph(odd_degree_nodes)
    
    # Step 3: Find minimum-weight perfect matching
    matching_edges = max_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')
    
    # Step 4: Combine edges of T and matching to form a multigraph
    multigraph = T.copy()
    multigraph.add_edges_from(matching_edges)
    
    # Step 5: Find an Eulerian circuit
    circuit = list(eulerian_circuit(multigraph))
    
    # Step 6: Convert Eulerian to Hamiltonian
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Complete the tour by returning to the start
    
    return path

# Main function to solve TSP
def solve_tsp(cities):
    G = create_graph(cities)
    tour = christofides_algorithm(G)
    
    # Compute the travel cost of the tour
    total_travel_cost = sum(
        euclidean(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1)
    )
    
    return tour, total_travel_cost

# Execute function
tour, total_travel_cost = solve_tsp(cities)
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)