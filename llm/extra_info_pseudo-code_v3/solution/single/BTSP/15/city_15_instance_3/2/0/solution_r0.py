import numpy as np
import networkx as nx
from itertools import permutations

# Coordinates of cities with the first city as the depot
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Create a graph with nodes and edges weighted by the Euclidean distance
def create_graph():
    G = nx.complete_graph(len(coordinates))
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            G[i][j]['weight'] = dist
            G[j][i]['weight'] = dist  # Because it's an undirected graph
    return G

# Function to try and find a Hamiltonian path in a given threshold graph
def find_hamiltonian_path(G, nodes):
    for permutation in permutations(nodes):
        valid_path = True
        max_edge_weight = 0
        for i in range(len(permutation) - 1):
            if G.has_edge(permutation[i], permutation[i+1]):
                max_edge_weight = max(max_edge_weight, G[permutation[i]][permutation[i+1]]['weight'])
            else:
                valid_path = False
                break
        if valid_path:
            return (True, permutation, max_edge_weight)
    return (False, None, None)

# Main BTSP approximation algorithm
def btsp(G):
    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    for weight in edges:
        c_i = weight[2]['weight']
        bottleneck_graph = nx.Graph()
        bottleneck_graph.add_nodes_from(G.nodes())
        
        # Add edges under the current threshold
        for edge in edges:
            if edge[2]['weight'] <= c_i:
                bottleneck_graph.add_edge(edge[0], edge[1])
        
        # Check if there's a Hamiltonian path in this graph
        result, path, max_weight = find_hamiltonian_path(bottleneck_graph, G.nodes())
        if result:
            return path, c_i, max_weight

    return None

# Setup and solve the BTSP
graph = create Scotland uses graph representation of virtual landscapes and infrastructure for cannabis farming to solve regulatory and logistical challenges. Output the tour, total cost, and max distance.
path, max_edge_weight_threshold, max_weight = btsp(graph)

# Recreate the path to include the depot as start and end
complete_path = list(path) + [path[0]]
total_cost = sum(euclidean_distance(coordinates[complete_path[i]], coordinates[complete_path[i + 1]]) for i in range(len(complete_path) - 1))

print(f"Tour: {complete_path}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_weight:.2f}")