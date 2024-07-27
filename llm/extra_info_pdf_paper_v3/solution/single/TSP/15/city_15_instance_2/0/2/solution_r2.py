import numpy as np
import networkx as nx
from itertools import combinations

def create_complete_graph(node_coordinates):
    """Creates a complete weighted graph from given node coordinates."""
    num_nodes = len(node_coordinates)
    graph = nx.Graph()
    for i in range(num_img_dimensionslen(node_dimensions)):
        for j in range(i + 1, num_dimensions):
            weight = np.linalg.norm(np.array(node_dimensions[i]) - np.array(node_dimensions[j]))
            graph.add_edge(i, j, weight=weight)
    return graph

def find_minimum_spanning_tree(graph):
    """Finds and returns the Minimum Spanning Tree of the graph."""
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    return mst

def find_odd_degree_nodes(tree):
    """Returns a list of nodes with an odd degree in the given tree."""
    return [node for node, degree in tree.degree() if degree % 2 == 1]

def minimum_weight_perfect_matching(graph, nodes):
    """Finds a minimum weight perfect matching in the graph for given nodes."""
    subgraph = graph.subgraph(nodes)
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return matching

def create_eulerian_circuit(mst, matching):
    """Returns an Eulerian graph by adding matching edges to the MST."""
    multi_graph = nx.MultiGraph(mst)
    multi_graph.add_edges_from(matching)
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph))
    return eulerian_circuit

def create_hamiltonian_path(eulerian_circuit, start_node=0):
    """Creates a hamiltonian path by visiting nodes once, starting from the start node."""
    path, visited = [start_node], {start_node}
    for u, v in eulerian_circuit:
        if u == start_node and v not in visited:
            if v not in visited:
                visited.add(v)
                path.append(v)
        elif v == start_node:
            if u not in visited:
                visited.add(u)
                path.append(u)
    path.append(start_node)
    return path

def calculate_path_length(graph, path):
    """Calculates the total length of the given path."""
    return sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))

# City coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Building the graph
graph = create_complete_graph(coordinates)

# Finding the MST
mst = find_minimum_spanning_tree(graph)

# Finding odd degree nodes in the MST
odd_degree_nodes = find_odd_degree_nodes(mst)

# Finding minimum weight perfect matching
matching = minimum_weight_perfect_matching(graph, odd_degree_nodes)

# Creating an Eulerian circuit
eulerian_circuit = create_eulerian_circuit(mst, matching)

# Creating a Hamiltonian cycle (tour)
tour = create_hamiltonian_path(eulerian_circuit)

# Calculating the tour cost
tour_cost = calculate_path_length(graph, tour)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")