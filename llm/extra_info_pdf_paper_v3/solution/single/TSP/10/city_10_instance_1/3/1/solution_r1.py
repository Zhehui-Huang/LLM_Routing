import math
from itertools import combinations
import networkx as nx

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def construct_graph(cities):
    """Construct the graph with all possible edges and their distances."""
    G = nx.Graph()
    n = len(cities)
    for u in range(n):
        for v in range(u + 1, n):
            G.add_edge(u, v, weight=euclidean_distance(cities[u], cities[v]))
    return G

def find_minimum_weight_perft_matching(H):
    """Find a minimum weight perfect matching for the given graph."""
    # This min weight matching might not be trivial to implement from scratch; use networkx method as a placeholder
    return nx.algorithms.matching.min_weight_matching(H, maxcardinality=True)

def christofides_algorithm(cities):
    """Implement the Christofides algorithm to find an approximate TSP tour."""
    G = construct_graph(cities)
    T = nx.minimum_spanning_tree(G)
    
    # Find vertices of odd degree in T
    odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]
    
    # Create a subgraph H induced on vertices of odd degree
    H = G.subgraph(odd_degree_nodes)
    
    # Find a minimum weight perfect matching on H
    M = find_minimum_weight_perft_matching(H)
    
    # Combine the edges of T and M to form a multigraph
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(M)
    
    # Find an Eulerian circuit in the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))
    
    # Convert the Eulerian circuit to a Hamiltonian path (shortcutting)
    path, visited = [], set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to return to the start point
    
    return path

# Define the cities
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), 
          (70, 14), (97, 44), (17, 69), (95, 89)]

# Solve TSP using Christofides' algorithm
tour = christofides_algorithm(cities)

# Calculate the tour cost:
tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Print out the tour and the total travel cost
print("Tour:", tour)
print("Total travel cost:", tour_cost)