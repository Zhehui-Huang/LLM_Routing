import numpy as np
import networkx as nx
import math
from scipy.spatial import distance_matrix
from itertools import combinations

# ---------------------------------------------------------------------
# City coordinates
# ---------------------------------------------------------------------
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# ---------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a complete graph with weights representing the distances
def create_complete_graph(node_list, weight_func):
    G = nx.Graph()
    for u, v in combinations(node_list, 2):
        G.add_edge(u, v, weight=weight_func(u, v))
    return G

# Compute a minimum weight perfect matching
def minimum_weight_matching(G, odd_vertices):
    result = nx.Graph()
    for u, v in combinations(odd_vertices, 2):
        result.add_edge(u, v, weight=G[u][v]['weight'])
    return nx.algorithms.matching.min_weight_matching(result, maxcardinality=True)

# Find Eulerian circuit
def find_eulerian_circuit(G, source):
    return list(nx.eulerian_circuit(G, source=source))

# ---------------------------------------------------------------------
# Christofides algorithm
# ---------------------------------------------------------------------

def christofides_tsp(node_list, weight_func):
    # Create the complete graph with the distances as edge weights
    G = create_complete_graph(node_list, weight_func)
    
    # Compute the minimum spanning tree (MST)
    T = nx.minimum_spanning_tree(G)
    
    # Identify vertices with odd degree in the MST
    odd_degree_nodes = [v for v in T.nodes() if T.degree(v) % 2 != 0]
    
    # Find a minimum weight perfect matching for the odd degree vertices
    matched_edges = minimum_weight_matching(G, odd_degree_nodes)
    
    # Add matched edges to the MST to create a multigraph
    H = T.copy()
    H.add_edges_from(matched_edges)
    
    # Find an Eulerian circuit in the multigraph
    euler_circuit = find_eulerian_circuit(H, source=node_list[0])
    
    # Convert the Eulerian circuit to a Hamiltonian circuit
    seen = set()
    path = []
    for u, v in euler_circuit:
        if u not in seen:
            path.append(u)
            seen.add(u)
    path.append(path[0])  # Close the tour
    
    return path, nx.path_weight(G, path, weight='weight')

# ---------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------

# Convert city tuples to a list for processing
node_list = list(range(len(cities)))

# Compute the tour and cost
tour, cost = christofides_tsp(node_list, lambda u, v: euclidean_distance(cities[u], cities[v]))

# Output the resulting tour and total cost
print("Tour:", tour)
print("Total travel cost:", cost)