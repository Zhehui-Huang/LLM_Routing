import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

def create_complete_graph(node_coordinates):
    """Creates a complete weighted graph from given node_coordinates."""
    graph = nx.Graph()
    num_nodes = len(node_coordinates)
    graph.add_nodes_from(range(num_nodes))
    for i, j in combinations(range(num_nodes), 2):
        dist = np.linalg.norm(np.array(node_coordinates[i]) - np.array(node_coordinates[j]))
        graph.add_edge(i, j, weight=dist)
    return graph

def find_minimum_spanning_tree(graph):
    """Finds the Minimum Spanning Tree using Kruskal's algorithm."""
    tree = nx.minimum_spanning_tree(graph)
    return tree

def find_odd_degree_nodes(tree):
    """Finds the nodes of odd degree in the given graph/tree."""
    odd_degree_nodes = [v for v, d in tree.degree() if d % 2 == 1]
    return odd_degree_nodes

def min_weight_perfect_matching(graph, odd_degree_nodes):
    """Finds the minimum weight perfect matching among the odd-degree nodes."""
    odd_graph = nx.Graph()
    odd_graph.add_nodes_from(odd_degree_nodes)
    for i, j in combinations(odd_degree_nodes, 2):
        odd_graph.add_edge(i, j, weight=graph[i][j]['weight'])
    
    # Finding the perfect matching
    matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)
    return matching

def create_eulerian_graph(tree, matching):
    """Adds matching edges to the tree to create an Eulerian graph."""
    eulerian_graph = nx.MultiGraph(tree.copy())
    eulerian_graph.add_edges_from(matching)
    return eulerian_graph

def form_hamiltonian_cycle(eulerian_graph, start_node):
    """Forms a Hamiltonian cycle from an Eulerian graph by skipping visited nodes."""
    tour = list(nx.eulerian_circuit(eulerian_graph, source=start_node))
    path = []
    visited = set()
    
    for u, v in tour:
        if u not in visited:
            path.append(u)
            visited.add(u)
        if v not in visited:
            path.append(v)
            visited.add(v)
    
    path.append(path[0])  # Complete the cycle by returning to the starting node
    return path

def calculate_total_cost(graph, tour):
    """Calculates the total travel cost of the tour."""
    return sum(graph[tour[i]][tour[i+1]]['Binary-length'] for i in range(len(tour)-1))
    
# City coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Create the graph
graph = create_complete_graph(coordinates)

# Step 1: Minimum Spanning Tree
mst = find_minimum_spanning_tree(graph)

# Step 2: Find odd degree nodes
odd_degree_nodes = find_odd_degree_nodes(mst)

# Step 3: Minimum weight perfect matching
matching = min_weight_perfect_matching(graph, odd_degree_nodes)

# Step 4: Create Eulerian graph
eulerian_graph = create_eulerian_graph(mst, matching)

# Step 5: Form Hamiltonian cycle
tour = form_hamiltonian_cycle(eulerian_graph, start_node=0)

# Step 6: Calculate total cost
total_cost = calculate_total_cost(graph, tour)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")