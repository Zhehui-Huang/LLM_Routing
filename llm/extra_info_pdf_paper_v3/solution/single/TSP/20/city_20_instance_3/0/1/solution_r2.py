import numpy as np
import networkx as nx
from scipy.spatial import distance

def create_graph(cities):
    """Create a complete graph from given city coordinates."""
    G = nx.Graph()
    num_cities = len(cities)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = distance.euclidean(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

def find_minimum_spanning_tree(G):
    """Find the minimum spanning tree of the graph using Kruskal's algorithm."""
    return nx.minimum_spanning_tree(G, weight='weight')

def find_odd_degree_nodes(MST):
    """Find nodes that have an odd degree in the MST."""
    return [node for node, degree in MST.degree() if degree % 2 == 1]

def add_minimum_weight_matching(MST, G, odd_nodes):
    """Add minimum weight matching edges from the original graph G to the MST for odd degree nodes."""
    subgraph = G.subgraph(odd_nodes)
    matching_edges = nx.algorithms.max_weight_matching(subgraph, maxcardinality=True, weight='weight')
    MST.add_edges_from(matching_edges)

def eulerian_circuit_to_hamiltonian_circuit(G, circuit):
    """Convert Eulerian circuit to Hamiltonian circuit by skipping repeated nodes."""
    visited = set()
    path = []
    for node in circuit:
        if node not in visited:
            visited.add(node)
            path.append(node)
    path.append(path[0])  # complete the tour by returning to the start
    return path

def find_total_distance(G, tour):
    """Calculate the total weight (distance) of the tour."""
    return sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

# Coordinates of the cities
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Step by step computation
graph = create_graph(cities)
mst = find_minimum_spanning_tree(graph)
odd_degree_nodes = find_odd_degree_nodes(mst)
add_minimum_weight_matching(mst, graph, odd_degree_async_nodes)
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))
hamiltonian_tour = eulerian_circuit_to_hamiltonian_circuit(graph, [u for u, v in eulerian_circuit])
total_cost = find_total_distance(graph, hamiltonian_tour)

# Outputting the tour and the total distance
print("Tour:", hamiltonian_tour)
print("Total travel cost:", round(total_cost, 2))