import math
import networkx as nx

# City coordinates
coords = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two points
def euclidean_distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

# Create a complete weighted graph
def create_graph():
    graph = nx.Graph()
    for i in coords:
        for j in coords:
            if i != j:
                graph.add_edge(i, j, weight=euclidean_distance(i, j))
    return graph

# Algorithm to find bottleneck-optimal biconnected subgraph
def find_biconnected_subgraph(graph):
    edges_sorted = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    biconnected_subgraph = nx.Graph()
    biconnected_subgraph.add_nodes_from(graph.nodes())
    
    for edge in edges_sorted:
        biconnected_subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(biconnected_subgraph):
            return biconnected_subgraph
    
    return biconnected_subgraph  # Fallback, should not happen

# Function to find tour in squared graph
def find_hamiltonian_cycle(biconnected_subgraph):
    squared_graph = nx.algorithms.operators.binary.power(biconnected_subgraph, 2)
    cycle = nx.approximation.tsp.christofides(squared_graph)
    return cycle

# Main execution
graph = create_graph()
biconnected_subgraph = find_biconnected_subgraph(graph)
tour = find_hamiltonian_cycle(biconnected_subgraph)

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
maximum_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Outputting results
output = {
    "Tour": tour + [tour[0]],
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": maximum_distance
}

print(output)