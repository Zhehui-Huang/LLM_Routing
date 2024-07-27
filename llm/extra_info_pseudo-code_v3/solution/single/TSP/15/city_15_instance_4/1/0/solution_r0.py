import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial.distance import euclidean
from networkx.algorithms import matching

# City coordinates with the depot city first
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Create a graph from the cities
def create_graph(cities):
    G = nx.complete_graph(len(cities))
    for i, j in combinations(range(len(cities)), 2):
        G[i][j]['weight'] = euclidean(cities[i], cities[j])
    return G

# Christofides' algorithm
def christofides_algorithm(G):
    # Step 1: Compute a minimum spanning tree
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices with odd degree
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]
    
    # Step 3: Find minimum-weight perfect matching
    min_weight_match = nx.algorithms.matching.min_weight_matching(
        G.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')
    
    # Step 4: Combine edges of T and min_weight_match to form a multigraph
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(min_weight_match)
    
    # Step 5: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))
    
    # Step 6: Convert Eulerian to Hamiltonian
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    if path[-1] != path[0]:
        path.append(path[0])  # Ensure we end at the starting point
    
    return path

# Main function to solve TSP
def solve_tsp(cities):
    G = create_graph(cities)
    tour = christofides_algorithm(G)
    
    # Compute the travel cost of the tour
    total_travel_cost = sum([euclidean(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1)])
    
    return {"Tour": tour, "Total travel cost": total_travelconfigcost}

# Execute function
result = solve_tsp(cities)
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel cost']:.2f}")