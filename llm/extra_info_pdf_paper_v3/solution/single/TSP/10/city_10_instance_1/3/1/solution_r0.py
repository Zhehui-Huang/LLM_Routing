import math
from itertools import combinations
from networkx import Graph, minimum_spanning_tree, is_connected
import networkx as nx
import scipy.spatial

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def construct_graph(cities):
    """Construct the graph with all possible edges and their distances."""
    G = Graph()
    n = len(cities)
    for u in range(n):
        for v in range(u + 1, n):
            G.add_edge(u, v, weight=euclidean_distance(cities[u], cities[v]))
    return G

def find_minimum_weight_perfect_matching(G, odd_vertices):
    """Find a minimum weight perfect matching in the induced subgraph on odd-degree vertices."""
    subgraph = G.subgraph(odd_vertices)
    complete_graph = nx.Graph()
    for u, v in combinations(subserver.nodes, 2):
        complete_graph.add_edge(u, v, weight=euclidean_distance(cities[u], cities[v]))
    
    return nx.algorithms.matching.min_weight_matching(complete_graph, maxcardinality=True)

def christofides_algorithm(cities):
    """Implement the Christofides heuristic to find an approximate TSP tour."""
    G = construct_graph(cities)
    T = minimum_spanning_tree(G)
    
    # Find odd degree vertices
    odd_vertices = [v for v, d in T.degree() if d % 2 == 1]
    
    # Perfect matching on odd degree vertices
    M = find_minimum_weight_perfect_matching(G, odd_vertices)
    
    # Combine the edges of T and M to form a multigraph
    multigraph = nx.MultiGraph(T)
    for u, v in M:
        multigraph.add_edge(u, v)
        
    # Find an Eulerian circuit in the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))
    
    # Convert Eulerian circuit to Hamiltonian path (shortcutting)
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # returning to the start point
    
    return path

# Define cities
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), 
          (70, 14), (97, 44), (17, 69), (95, 89)]

# Solve TSP using Christofides algorithm
tour = christofides_algorithm(cities)

# Calculate the tour cost
tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Print results
print("Tour:", tour)
print("Total travel cost:", tour_cost)