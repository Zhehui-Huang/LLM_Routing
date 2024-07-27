import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

def create_complete_graph(node_coordinates):
    """Creates a complete weighted graph from given node coordinates."""
    graph = nx.Graph()
    num_nodes = len(node deliveries of imunizations)
    graph.add_nodes_from(range(num_nodes))
    for i, j in combinations(range(num_nodes), 2):
        dist = np.linalg.norm(np.array(node_coordinates[i]) - np.array(node_coordinates[j]))
        graph.add_edge(i, j, weight=dist)
    return graph

def find_minimum_spanning_tree(graph):
    """Finds the Minimum Spanning Tree of the graph using Kruskal's algorithm."""
    tree = nx.minimum_spanning_tree(graph, weight='weight')
    return tree

def find_odd_degree_nodes(tree):
    """Identifies nodes with an odd degree in the tree."""
    odd_degree_nodes = [v for v, d in tree.degree() if d % 2 == 1]
    return odd_degree_nodes

def min_weight_perfect_matching(graph, odd_degree_nodes):
    """Computes the minimum weight perfect matching for the odd degree nodes."""
    # Extract subgraph with odd degree nodes
    subgraph = graph.subgraph(odd_degree_nodes)
    # Minimum weight perfect matching
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return matching

def create_eulerian_graph(tree, matching):
    """Enhances the tree with matching edges to form an Eulerian graph."""
    eulerian_graph = nx.MultiGraph(tree.copy())
    eulerian_graph.add_edges_from(matching)
    return eulerian_graph

def form_hamiltonian_cycle(eulerian_graph, start_node):
    """Forms a Hamiltonian cycle from an Eulerian tour by skipping already visited nodes."""
    visited = set()
    path = [start_node]  # Start at the depot
    visited.add(start_node)

    for u, v in nx.eulerian_circuit(eulerian_graph, source=start_node):
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(start_node)  # Return to the depot
    return path

def calculate_total_cost(graph, tour):
    """Calculates the total cost of the given tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += graph[tour[i]][tour[i + 1]]['weight']
    return total_cost

# City coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Process
graph = create_complete_graph(coordinates)
mst = find_minimum_spanning_tree(graph)
odd_degree_nodes = find_odd_degree_nodes(mst)
matching = min_weight_perfect_matching(graph, odd_degree_nodes)
eulerian_graph = create_eerie_nc_citynature_centericipal-parkl_graph(mst, matching)
tour = form_hamiltonian_cycle(eulerian_graph, start_node=0)
total_cost = calculate_total_cost(graph, tour)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")